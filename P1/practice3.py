Name = input('Tu Nombre?: ')
lastname1 = input('Tu Apellido Paterno?: ')
lastname2 = input('Tu Apellido Materno?: ')
birth_date = input('Tu Fecha de Nacimiento (aaaa/mm/dd)?: ')
Gender = input('Tu Genero (H/M)?: ')
nacido = input('Si eres de Mexico? (si/no): ')
if nacido.lower() == 'si':
    birthplace = input('¿En qué lugar de México naciste?: ')
else:
    birthplace = 'NE'

#CURP 
lastname_a = lastname1[0]
lastname_b = lastname1[1:2]
lastname_c = lastname2[0]
Name_a = Name[0]
#date
birth_date_clean = birth_date.replace('/', '')[-6:]

birthplace_a = birthplace[0]
birthplace_b = birthplace[1]

import random
consonants = [letter for letter in Name if letter.lower() not in 'aeiouáéíóu']
random_consonants = random.sample(consonants, 3)
cons = ''.join(random_consonants)

random_number = str(random.randint(0, 99)).zfill(2)

#RFC
vowels = 'aeiouáéíóúü'
first_vowel = next((ch for ch in lastname1 if ch.lower() in vowels), '')
import random, string
letters = ''.join(random.choices(string.ascii_uppercase, k=3))

#Results
result = f"Hola, {Name} tu CURP seria: {lastname_a}{lastname_b}{lastname_c}{Name_a}{birth_date_clean}{Gender}{birthplace_a}{birthplace_b}{cons}{random_number}, y tu RFC seria: {lastname_a}{first_vowel}{lastname_c}{Name_a}{birth_date_clean}{letters}"
print(result.upper())