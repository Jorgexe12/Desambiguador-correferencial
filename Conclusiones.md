## Tokenización
Durante la tokenización hemos usado el word_tokenize. Además hemos probado algunos stemmer de nltk como el lancaster y el snowball.

Probando los stemmers intentábamos sacar las raices verbales para así sacar los clíticos de los verbos. Sin embargo, cuando los verbos presentaban estos clíticos, los stemmers no sacaban la raíz verbal de forma correcta siendo que es inevitable preprocesar el texto de forma manual.

Para ello la opción más razonable que encontramos fue la de hacer una lista de reglas con los verbos más comunes y sus formas imperativas además de los metadatos de cómo debería ser reconocido por el modelo para etiquetar.

Nos quedamos finalmente con la tokenización basada en reglas.

# Preprocesamiento
Hemos probado SpaCy, Stanza y Flair para sacar las etiquetas part-of-speech. Los problemas de spacy, stanza y flair son esencialmente los mismos aunque con distintos grados de inconsistencias, pero esencialmente son que no son capaces de separar los clíticos de las formas imperativas de los verbos. Fuera de esto etiquetan bastante bien las diferentes palabras de un texto.  
Entre Stanza, SpaCy y Flair al final nos decantamos por stanza por comodidad aunque spacy también nos habría servido para este proyecto.


Como conclusiones al preprocesamiento podemos sacar que ninguno de los modelos actuales procesa bien los clíticos verbales en formas imperativas y que debido a que al tokenizar eliminan las tildes, también les cuesta distiguir entre verbos con formas similares como comer y cometer.

## Formateo de datos

Durante el formateo de datos nos hemos decantado por el formato conllu puro, que es el formato que aceptan los modelos Roberta. Para ello, hemos creado funciones que recibiendo ya el texto tokenizado por Stanza, lo convierten al formato necesario para el modelo y luego se guarda en un archivo a parte que se usará como entradas al modelo ya sea para entrenarlo o para probarlo.

Cabe recalcar que si el dataset que se emplea es de texto ya tokenizado, este no será necesario pasarlo por el preprocesamiento pero si por el formateo.

# Modelo

El modelo se trata de un modelo Roberta cuyo objetivo será resolver las correferencias de los pronombres del texto agrupándolos en clusters.

## Entrenamiento

Para el entrenamiento era necesario entrenarlo con frases, o bien que tuvieran correferencias dentro de ella, o bien que tuvieran correferencias entre ellas. Lamentablemente no hemos podido entrenar el modelo todo lo bien que querríamos porque se nos hacía inviable el tiempo que tardaba ya que eran 10h por época en colab. Al final lo entrenamos con muchos menos datos y el modelo no está cerca de aprender las correferencias correctamente.  
Aún así pensamos que con un gran computador y el suficiente tiempo se podría entrenar el modelo correctamente.

Después de bastante quebraderos de cabeza, el último día nos dimos cuenta que los datos que preprocesamos y los que necesita el modelo eran distintos, pero ya era muy tarde para cambiarlos. Debido a eso, no pudimos determinar si fallaba algo del modelo o solo era esa incompatiblidad cuando depurábamos.

## Prueba

Debido a los fallos mencionados anteriormente en el entrenamiento, no pudimos sacar conclusiones válidas del modelo ya que nos agrupaba todo en un mismo cluster de referencia y, debido a la falta de tiempo, no pudimos corregirlo.