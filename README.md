# Desambiguador-correferencial
Proyecto de la asignatura PLN.  
Autores: Jorge Aured Zarzoso, Iván García Adell, Iván Pastor Sacristán.

En este proyecto hemos sacado las etiquetas part-of-speech de un texto (POS TAG); hemos pasado el texto etiquetado a formato conllu; hemos entrenado un modelo (NOMBRE) para predecir a qué sustantivos hacen referencia los pronombres; ...

Tenemos diversos notebooks, cada uno con una parte del proceso. Además, tenemos un notebook inicial llamado requirements en el cual solo existe un comando pip para instalar todas las dependencias del proyecto, recomendamos el uso de un entorno virtual. El orden de los archivos es el siguiente:
1 requirements -> 2 prerpocesar (POS TAG + reglas) -> 3 formatear -> 4 entrenar -> 5 predecir -> 6 (TERCERA PATA PLN?) -> 7 conclusiones.  
Además, tenemos varios archivos, vamos a explicar cada uno, en orden, y de dónde sale:
- requirements.txt: guarda la información de todas las librerías que usamos en el proyecto.
- CulturaX.json: tiene 5000 filas del dataset CulturaX de HuggingFace, este subset será el que usemos para sacar las etiquetas.
- patterns.json: tiene un conjunto de reglas con verbos con enclíticos para poder aplicar en preprocesado.
- entrada.conllu: es el archivo de entrada de las predicciones del modelo que resuelve las referencias. Sale del archivo CulturaX y es un subset de este por tema de tiempos en preprocesar.