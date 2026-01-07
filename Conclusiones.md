# Preprocesado
El preprocesado se ha basado en recibir un archivo de texto, aplicarle el pos-tagging y luego darle formato conllu para pasárselo al modelo.

## Tokenización
Durante la tokenización hemos probado distintos tokenizadores como spacy, stanza y flair. Además hemos probado algunos stemmer de nltk como el lancaster y el snowball.

Los problemas de spacy, stanza y flair son esencialmente los mismos aunque con distintos grados de inconsistencias, pero esencialmente son que no son capaces de separar los clíticos de las formas imperativas de los verbos.

Probando los stemmers intentábamos sacar las raices verbales para así sacar los clíticos de los verbos. Sin embargo, cuando los verbos presentaban estos clíticos, los stemmers no sacaban la raíz verbal de forma correcta siendo que es inevitable preprocesar el texto de forma manual.

Para ello la opción más razonable que encontramos fue la de hacer una lista de excepciones con los verbos más comunes y sus formas imperativas además de las reglas de como debería ser reconocido por el tokenizador.

Entre stanza y spacy al final nos decantamos por stanza por comodidad porque spacy también nos habría servido para este proyecto.

Como conclusiones al tokenizado podemos sacar que ninguno de los modelos actuales procesa bien los clíticos verbales en formas imperativas y que debido a que al tokenizar eliminan las tildes, también les cuesta distiguir entre verbos con formas similares como comer y cometer. 

## Formateo de datos

Durante el formateo de datos nos hemos decantado por el formato conllu puro, que es el formato que aceptan los modelos Roberta. Para ello, hemos creado funciones que recibiendo ya el texto tokenizado por stanza, lo convierten al formato necesario para el modelo y luego se guarda en un archivo a parte que se usará como entradas al modelo ya sea para entrenarlo o para probarlo.

Cabe recalcar que si el dataset que se emplea es de texto ya tokenizado, este no será necesario pasarlo por el preprocesamiento pero si por el formateo.

# Modelo

El modelo se trata de un modelo Roberta cuyo objetivo será resolver las correferencias de los pronombres del texto.

## Entrenamiento



## Prueba
