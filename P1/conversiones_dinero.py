"""EMILY SANDOVAL MADERO ,2I, 3 marzo 2026"""
#Conversor de divisas
#calcular la equivalencia de cada divisa en base a un valor dado por el usuario

#china
yuan=0.14
#japon
yen=0.0063
#Estados Unidos
dolar=1
#union europea
euro=1.16
#Reino Unido
libra=1.33
#Pesos
mxn = 0.057

pesos = input("Ingresa la cantidad de pesos a convertir: ")
usd = float(pesos) * mxn
print("Los pesos equivalen a ")
print(f"En dólares: {usd}")
print(f"En yuanes: {usd / yuan}")
print(f"En yenes: {usd / yen}")
print(f"En euros: {usd / euro}")
print(f"En libras: {usd / libra}")

"""Resultado converosr divisas"""
Ingresa la cantidad de pesos a convertir: 1
Los pesos equivalen a 
En dólares: 0.057
En yuanes: 0.40714285714285714
En yenes: 9.047619047619047/conversiones_listas.py 
En euros: 0.04913793103448277
En libras: 0.04285714285714286