###### Arrancamos ######
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance

## Lee archivo y listas de preguntas
def CargaPreguntas(archivo):
	f = open(archivo,"r")
	texto = f.read()
	pregs = sent_tokenize(texto)
	return (texto,pregs)

## Eliminar las "stopwords"
def getCleanQs(listaOracion):
	stopws = stopwords.words("spanish")
	## Eliminar las no alfabeticas
	textoconsw = [w.lower() for w in listaOracion if w.isalpha() ]
	textosinsw = [w for w in textoconsw if w not in stopws]
	return textosinsw

## Generar los vectores, para saber que palabra importante esta preguntando
## en el diccionario vienen todas las palabras, la de la pregunta que se repite es el tema 
## que pregunta
def crearVector(oracion,diccionario):
	distrib = nltk.FreqDist(oracion)
	vector = [distrib[w] for w in diccionario]
	return vector 

def cargaRespuesta(archivo,indice):
	f = open(archivo,"r")
	texto = f.read()
	res = sent_tokenize(texto)
	return (res[indice])

## Leer corpus de preguntas
(ptxt,psucias) = CargaPreguntas("preg2.txt")

## Convertir de oraciones a palabras
qsWords = [ word_tokenize(orac) for orac in psucias ]

## Eliminamos las stopwords
tssw = [getCleanQs(orac) for orac in qsWords]

pu =input("Dime >>")

## determinar el diccionario
texto_tot = getCleanQs(word_tokenize(ptxt) + word_tokenize(pu))
dicc = set(texto_tot)

## crear vectores
vs=[crearVector(ora,dicc) for ora in tssw]

## crea vector pregunta de usuario
vpu = crearVector(getCleanQs(word_tokenize(pu)),dicc)

##calcula similitudes
sims = [((cosine_distance(vpu,v)-1)*(-1)) for v in vs]
indice = sims.index(max(sims))
print(cargaRespuesta("res2.txt",indice))