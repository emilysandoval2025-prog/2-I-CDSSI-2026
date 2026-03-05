"""Emily Sandoval Madero, 2I, 3 marzo 2026"""
#Zonas Horarias
#Calcular la hora de las ciudades a base de la hora especificada por el usuario
#Cabe considerar que la hora sera representada en un sistema de 12 horas

dublin = 0
paris = 1
londres = 0
tokio = 9
los_angeles = -8
nueva_york = -5
nueva_deli = 5
cdmx = -6

hora = int(input("Ingresa la hora (1-12): "))

print("La hora en las siguientes ciudades seria: ")
print("Dublin: " + str(hora) + " horas")
print("Paris: " + str(hora + paris) + " horas")
print("Londres: " + str(hora + londres) + " horas")
print("Tokio: " + str(hora + tokio) + " horas")
print("Los Angeles: " + str(hora + los_angeles) + " horas")
print("Nueva York: " + str(hora + nueva_york) + " horas")
print("Nueva Delhi: " + str(hora + nueva_deli) + " horas")
print("CDMX: " + str(hora + cdmx) + " horas")

"""Resultado Zonas Horarias"""
Ingresa la hora (1-12): 3
La hora en las siguientes ciudades seria: 
Dublin: 3 horas
Paris: 4 horas
Londres: 3 horas
Tokio: 12 horas
Los Angeles: -5 horas
Nueva York: -2 horas
Nueva Delhi: 8 horas
CDMX: -3 horas