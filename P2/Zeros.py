#"EMILY SANDOVAL MADER 2I 10 of March of 2026"
class TresSumaCero:

    def encontrar_tres(self, lista):
        lista.sort()
        resultado = []

        n = len(lista)

        for i in range(n - 2):
            izquierda = i + 1
            derecha = n - 1

            while izquierda < derecha:
                suma = lista[i] + lista[izquierda] + lista[derecha]

                if suma == 0:
                    resultado.append((lista[i], lista[izquierda], lista[derecha]))
                    izquierda += 1
                    derecha -= 1

                elif suma < 0:
                    izquierda += 1
                else:
                    derecha -= 1

        return resultado


# ejemplo de uso
lista = [-4, -1, -1, 0, 1, 2]

buscador = TresSumaCero()
print(buscador.encontrar_tres(lista))

class TresSumaCero:

    def encontrar_tres(self, lista):
        lista.sort()
        resultado = []

        n = len(lista)

        for i in range(n - 2):
            izquierda = i + 1
            derecha = n - 1

            while izquierda < derecha:
                suma = lista[i] + lista[izquierda] + lista[derecha]

                if suma == 0:
                    resultado.append((lista[i], lista[izquierda], lista[derecha]))
                    izquierda += 1
                    derecha -= 1

                elif suma < 0:
                    izquierda += 1
                else:
                    derecha -= 1

        return resultado


# ejemplo de uso
lista = [-4, -1, -1, 0, 1, 2]

buscador = TresSumaCero()
print(buscador.encontrar_tres(lista))

class TresSumaCero:

    def encontrar_tres(self, lista):
        lista.sort()
        resultado = []

        n = len(lista)

        for i in range(n - 2):
            izquierda = i + 1
            derecha = n - 1

            while izquierda < derecha:
                suma = lista[i] + lista[izquierda] + lista[derecha]

                if suma == 0:
                    resultado.append((lista[i], lista[izquierda], lista[derecha]))
                    izquierda += 1
                    derecha -= 1

                elif suma < 0:
                    izquierda += 1
                else:
                    derecha -= 1

        return resultado