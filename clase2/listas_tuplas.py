#listas
a=12

l=[3, 4,  5, 767, 8]
l1=[4.5, 7.8, 8.9]
l2=['h', 'o', 'l', 'a']
l3=[True, 'a', 5.67, 77, "labotec"]

#Acceder a listas
#print(l3[-1])

l4=[[3,4], True, [[6,7,"labotec",8]]]
#print(l4[2][0][2])

#extraccion de varios datos
l=[3, 4,  5, 767, 8]
#print(l[0:3])  #[inicio: final+1]
#print(l[1:])  #todos los valores hacia la derecha incluyendo el 5
#print(l[:4])  #todos los valores hacia la izquierda incluyendo el 767
#print(l[:-1])

l8=[1,2,3,4,5,6,7,8,9,10]
l8.append(11)
print(l8[0:10:2])   # [inicio: final: step]
print(l8[::-1])

#listas vacias
ll=[56] ##append()  
ll.append(3)   # agregar enteros a una lista
ll.append(67)
ll+[56,78]	  #sumar listas

print("ll contien: ",ll)

############################3
t=(1,2,3,34)	#tupla con parentesis
t1=45,67,89		#tupla sin parentesis
t2=()    		#tupla vacia
t3=(1,)          #tupla unitaria


