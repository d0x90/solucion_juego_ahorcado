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