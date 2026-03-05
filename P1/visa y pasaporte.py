"""
Emily Sandoval Madero 2"I 26/feb/2026
"""


print("Mensaje de bienvenida")
nombre=input("Cual es tu nombre?: ")
vigencia=input("Cuantos años deseas que sea valido tu pasaporte?\n" \
"           1- 1 año \n" \
"            2- 3 años \n" \
"            3- 6 años \n" \
"            4- 10 años \n")

destino=input("A que lugar quieres ir?\n1- USA\n2- Europa\n3- Japon\n4- Peru\n5- Canada,: ")
dolar=float(input("Cual es el valor del dolar en pesos hoy?"))
pasaporte = {"1": 920, #1 año
          "2": 1790, #3 años
          "3": 2440, #6 años
          "4": 4280, #10 años
}

costo=0
match destino:

    case "1":
        costo=185
    case "5":
        costo=100+85+7
    case "_":
        costo='0'
total=pasaporte.get(vigencia)+costo*dolar
print(f"{nombre} necesitas ${total} para tener tu visa y pasaporte")

"""
resultado
Mensaje de bienvenida
Cual es tu nombre?: emily
Cuantos años deseas que sea valido tu pasaporte?
           1- 1 año 
            2- 3 años 
            3- 6 años 
            4- 10 años 
2
A que lugar quieres ir?
1- USA
2- Europa
3- Japon
4- Peru
5- Canada,: 2
Cual es el valor del dolar en pesos hoy?17
emily necesitas $1790.0 para tener tu visa y pasaporte
PS C:\Users\Alumno>
"""