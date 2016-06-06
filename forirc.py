#a  c  e  r  t  a  m  i  e  n  t  _
import sys
import re
import sys
#CADENA (..*?)
#INICIO DE CADENA /\b()/
#FIN DE LA CADENA /()\b/
#cadena = sys.argv[1]
cadena = ""
count =0
for arg in sys.argv:
    if count != 0:
        cadena = cadena + arg
    count = count + 1


miregex = ""
micadenapararegex=""
mis_letras =set()
txt = open("palabras.txt").readlines()

def soloLetras(cadena,micadenapararegex):
	cadena.replace("_","")
	for c in cadena:
		mis_letras.add(c)
	for d in mis_letras:
		micadenapararegex = micadenapararegex + d
	return micadenapararegex.replace("_","")

micadenapararegex= soloLetras(cadena,micadenapararegex)
#print micadenapararegex
def proceso(miregex):
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
    #print miregex

    for linea in txt:
            m = re.search(miregex, linea)
            if m != None:
                    print m.group(0)

proceso(miregex)


