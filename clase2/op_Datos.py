#operaciones con enteros
#aritmeticas
import math

a=12.56
b=5.78

suma=a+b
restar=a-b
mult=a*b
div=a/b

"""
print('''
		la suma es:            {}
		la resta es:           {}
		la multiplicacion es:  {}
		la division es:        {} 
	  '''.format(suma,restar,mult, div))
"""

#otras operaciones
raiz=math.sqrt(a) #raiz,cuadrada
pot=math.pow(4,3) #potencia (base, exponente)
sen=math.sin(30*(3.1416/180))

"""
print(''' 
		raiz es: \t {}
		potencia es: \t {}
		seno de 30 es: \t {}
	'''.format(raiz,pot,sen))
"""


#-----------strings----------------------
s="hola"
m="mundo"

sm=s+' '+m
sp = (s+' ')*3

print('''
		suma: {}
		multi: {}
	'''.format(sm,sp))
	

d="moises"
dd = d.capitalize()
print("{} {}".format(d,dd))

print(len(d))
print(len(d))
	
#-----------------booleanos-----------------#
# and or
# >, <, ==, !=, <=, >=, 
b=True  #1
f=False #0

op1 = (b and f)  and (1==1) 
op2 = (b or f) and (13 == 10) and (14<=30) 

print(op1)
print(op2)






