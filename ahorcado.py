import re
import sys
## REGEX
##-------------------------
#CADENA (..*?)
#CADENA ([^asd]) sin a,s,d
#INICIO DE CADENA /\b()/
#FIN DE LA CADENA /()\b/
##-------------------------

#obteniendo argumento : python ahorcado.py <arg1>
cadena = sys.argv[1]
##variables
miregex = ""
micadenapararegex=""
mis_letras =set()
#diccionario
txt = open("palabras.txt").readlines()

### obtener las letras a evitar
def soloLetras(cadena,micadenapararegex):	
	for c in cadena:
		mis_letras.add(c)
	for d in mis_letras:
		micadenapararegex = micadenapararegex + d
	return micadenapararegex.replace("_","")

micadenapararegex= soloLetras(cadena,micadenapararegex)

#### Crear el regex
i = 0
arrCadena = cadena.split("_")
for pedazo in arrCadena:	
	if  i == 0:
		miregex= miregex+ ("\\b("+pedazo+")")

	elif i == len(arrCadena)-1:		
		miregex= miregex+ ("("+pedazo+")\\b")
		continue
	else:		
		miregex= miregex+ ("("+pedazo+")")
	miregex= miregex+ ("([^"+micadenapararegex+"])")
	i=i+1
print miregex

#procesamiento ( buscar en el diccionario las coincidencias)
for linea in txt:
	m = re.search(miregex, linea)
	if m != None:
		print m.group(0)