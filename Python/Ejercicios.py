""" personas = {
    "Juan": 28,
    "María": 15,
    "Pedro": 14,
    "Ana": 16,
    "Juan": 23,
    "Luis": 40,
    "Sofía": 17
}

print("Personas originales:", personas)
print()


mayores_de_edad = {
    nombre: edad for nombre, edad in personas.items() if edad >= 18}

ordenados = dict(sorted(mayores_de_edad.items(), key=lambda item: item[1]))

print("Personas mayores de edad ordenadas por edad:", ordenados)

# Numero primo entre 1 y 100

primo = []

fot i in range(1, 101):
    es_primo = True

    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            es_primo = False
            break
    if es_primo and i > 1:
        primo.append(i) """


num1 = 13

if num1 % 2 == 0:
    print(f"{num1} es par")
else:
    print(f"{num1} es impar")