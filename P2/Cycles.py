"""EMILY SANDOVAL MADERO 2'I 18 de marzo de 2026
"""
#-------------------------------------------------------------------------#
#Escribir un metodo que acepte el porcentaje de un alumno y evalue el grado de acuerdo al siguiente criterio
#Calificacion	Grado
#   >90				A
#   >80 y <= 90		B
#   >=60 y <=80		C
#   menor a 60		D
def evaluar_grado(porcentaje):
    if porcentaje > 90:
        return 'A'
    elif porcentaje > 80:
        return 'B'
    elif porcentaje >= 60:
        return 'C'
    else:
        return 'D'

#-------------------------------------------------------------------------#
#Escribir un metodo que capture el precio de una bicicleta y muestre los impuestos que debe pagar siguiendo los criterios siguientes:
# Costo					Impuesto
# >100000				15%
# >50000 y <= 100000	10% 
#<=50000				 5%
def calcular_impuesto(precio):
    if precio > 100000:
        impuesto = precio * 15
    elif precio > 50000:
        impuesto = precio * 10
    else:
        impuesto = precio * 5
    return impuesto

#-------------------------------------------------------------------------#
#Escribir un metodo que verifique si un año es bisiesto o no
def es_bisiesto(anio):
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        return True
    else:
        return False

#-------------------------------------------------------------------------#
#Escribir un metodo que capture un numero del 1 al 7 y muestre el nombre del dia de la semana
#Por ejemplo el 1 seria Domingo y el 2 Lunes
def dia_semana(num):
    dias = ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado']
    if 1 <= num <= 7:
        return dias[num - 1]
    else:
        return 'Número inválido'

#-------------------------------------------------------------------------#
#Escribir un metodo que acepte un numero del 1 al 12 y muestre el nombre del mes asi como los dias que contiene
#Ejemplo 1 seria Enero tiene 31 dias
def mes_info(num):
    meses = [
        ('Enero', 31),
        ('Febrero', 28), 
        ('Marzo', 31),
        ('Abril', 30),
        ('Mayo', 31),
        ('Junio', 30),
        ('Julio', 31),
        ('Agosto', 31),
        ('Septiembre', 30),
        ('Octubre', 31),
        ('Noviembre', 30),
        ('Diciembre', 31)
    ]
    if 1 <= num <= 12:
        nombre, dias = meses[num - 1]
        return f'{nombre} tiene {dias} días'
    else:
        return 'Número inválido'

#-------------------------------------------------------------------------#
#Escribir un programa que imprima los primeros 10 numeros naturales
def primeros_10_naturales():
    for i in range(1, 11):
        print(i)

#-------------------------------------------------------------------------#
#Escibir un programa que imprima los primeros 10 numeros impares
def primeros_10_impares():
    for i in range(1, 20, 2):
        print(i)
#-------------------------------------------------------------------------#
#Escribir un programa que imprima los primeros 10 numeros naturales en orden descendente
def primeros_10_descendente():
    for i in range(10, 0, -1):
        print(i)

#-------------------------------------------------------------------------#
#Escribir un programa que escriba la tabla de multiplicar de un numero especificado por el usuario
def tabla_multiplicar(num):
    for i in range(1, 11):
        print(f'{num} x {i} = {num * i}')
#-------------------------------------------------------------------------#
#Escribir un programa que escriba el producto de los digitos de un numero especificado por el usuario
def producto_digitos(num):
    producto = 1
    for digito in str(num):
        producto *= int(digito)
    return producto