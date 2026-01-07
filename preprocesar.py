import concurrent.futures
from tqdm.notebook import tqdm  # para progreso en notebooks
import stanza
import re
import json

with open('patterns.json', 'r', encoding='utf-8') as f:
    patterns = json.load(f)
    
CLITICS = ["me", "te", "se", "nos", "os", "lo", "la", "le", "los", "las", "les"]

def split_clitics(clitic_string: str, clitics_list: list = list()):
    clitics = []
    remaining = clitic_string

    for cl in clitics_list:
        if remaining.startswith(cl):
            clitics.append(cl)
            remaining = remaining[len(cl):]

    return clitics

def preprocess_imperatives(text: str):
    imperative_meta = []

    def make_replacer(pattern: str, rule: dict):
        regex = re.compile(pattern, flags=re.IGNORECASE)

        def replacer(match):
            groups = match.groups() # Analiza el patrón para buscar que clíticos coinciden
            # Mete los clíticos que coincidan en una lista como elementos separados
            clitic_string = "".join(g for g in groups if g) if groups else ""
            clitics = split_clitics(clitic_string, CLITICS)

            # Si no hay clíticos, no tocar la palabra original
            if not clitics:
                return match.group(0)
            

            replacement = " ".join([rule["base"]] + clitics)

            imperative_meta.append({
                "base": rule["base"],
                "lemma": rule["lemma"],
                "upos": rule["upos"]
            })

            # Mantener mayúscula inicial
            if match.group(0)[0].isupper():
                replacement = replacement.capitalize()

            return replacement

        return regex, replacer

    for pattern, rule in patterns.items():
        regex, replacer = make_replacer(pattern, rule)
        text = regex.sub(replacer, text)

    return text, imperative_meta

def preprocesar_paralelo(data: list, max_workers: int = 14):
    """
    Paraleliza el preprocesamiento de los textos para que sea más rápido
    """
    nlp = stanza.Pipeline(
        lang="es",
        processors="tokenize,mwt,pos,lemma,depparse",
        tokenize_pretokenized=False,
        use_gpu=True,
        verbose=False
    )
    
    def process_text(text):
        """Procesa un solo texto."""
        preprocessed, imperative_m = preprocess_imperatives(text)
        doc = nlp(preprocessed.lower())
        return doc, imperative_m
    
    docs = []
    imperative_meta = []
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_item = {executor.submit(process_text, item): item for item in data}
        
        for future in tqdm(concurrent.futures.as_completed(future_to_item), 
                          total=len(data), 
                          desc="Preprocesando"):
            try:
                doc, meta = future.result()
                docs.append(doc)
                imperative_meta.append(meta)
            except Exception as exc:
                print(f'Error procesando item: {exc}')
                # Agrega documentos vacíos para mantener el orden
                docs.append(None)
                imperative_meta.append([])
    
    return docs, imperative_meta