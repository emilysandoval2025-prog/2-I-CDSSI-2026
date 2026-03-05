#Emily Sandoval Madero 2I 4-Marzo-2026
#-------------------------------------------------------------------------#
#Crear una tupla con 3 elementos: 10, "Hola" y 3.14
tupla = (10, "hola", 3.14)
print(tupla)
#-------------------------------------------------------------------------#
#La tupla(1,2,3,4,5), accede y escribe el tercer elemento
tupla = (1,2,3,4,5)
print(tupla[2])
#-------------------------------------------------------------------------#
#Concatena las tuplas y almacena el resultado en una tupla Nueva
tupla1=("gato", "perro", "conejo")
tupla2=(1,2,3)
tupla_final=tupla1+tupla2
print(tupla_final)
#-------------------------------------------------------------------------#
#Desempaqueta la tupla en tres variables y escribe sus valores
tupla = ('a','b','c')
print(tupla[0],tupla[1],tupla[2])
#-------------------------------------------------------------------------#
#verifica si el elemento 7 existe en la tupla (1,3,5,7,9)
tupla = (1,3,5,7,9)
existe= 7 in tupla
print("existe")
#-------------------------------------------------------------------------#
#crea una tupla (0,1,2,3,4,5) y escribe los elementos del indice 2 a 4 con slice
tupla = (0,1,2,3,4,5)
resultado= tupla[2:5]
print(resultado)
#-------------------------------------------------------------------------#
#encuentra la longitude de una tupla (10,20,30,40,50)
tupla =  (10,20,30,40,50)
print(len(tupla))
#-------------------------------------------------------------------------#
#crea una tupla y repitela 3 veces
tupla_1= 4
resultado= tupla_1 * 3
print(resultado)
#-------------------------------------------------------------------------#
#convierte la lista[1,2,3] a tupla
lista= [1,2,3]
tupla=(lista)
print(tupla)
#-------------------------------------------------------------------------#
#Encuentra los valores minimo y maximo de la tupla(5,12,3,8,15)
min(tupla)
max(tupla)
print('Minimo: ',min(tupla),' Maximo: ', max(tupla))

(10, 'hola', 3.14)
3
('gato', 'perro', 'conejo', 1, 2, 3)
a b c
existe
(2, 3, 4)
5
12
[1, 2, 3]
Minimo:  1  Maximo:  3