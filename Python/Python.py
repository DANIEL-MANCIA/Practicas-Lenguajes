# ======================================
# Para imprimir algo en consola
# ======================================

print("Hola, Mundo!")

print("Hola Soy Daniel Mancia")
print()


# ====================================================
# Tipos de datos en Python(Basicos) y variables:
# se escriben en snake_case(Minusculas y guion bajo)
# ====================================================

saludo1 = "Hola Josue" # srtring
salaudo2 = 'Hola Daniel' # srt
saludo3 = "Hola" + " " + "Josue" + ' ' +'Mancia' # Concatenacion de String
print()

print("String con comillas dobles: " + saludo1)
print('String con comillas simples: ' + salaudo2)
print("Concatenacion de String: " + saludo3)
print()

num1_int = 10 # Entero
print(f"Dato Int: {num1_int}")

num2_float = 10.3 # Decimal
print(f"Dato Float: {num2_float}")

num3_bool_true = True # Booleano
print(f"Dato Bool_Verdadero: {num3_bool_true}")

num4_bool_false = False # Booleano
print(f"Dato Bool_Falso: {num4_bool_false}")

print()


# ============================================
# Verificar el tipo de dato de una variable,
# ============================================

print(type(saludo1)) # str
print(type(salaudo2)) # str
print(type(saludo3)) # str

print()

print(type(num1_int)) # int
print(type(num2_float)) # float
print(type(num3_bool_true)) # bool  
print(type(num4_bool_false)) # bool
print()

# Es posible declarar varias variables en una sola línea

nombre, apellido, edad = "Josue", "Mancia", 22
print(f"Nombre: {nombre}, Apellido: {apellido}, Edad: {edad}")
print()

# Se puede cambiar el tipo de una variable reasignándole un valor de otro tipo
edad = "Veintidos"
print(f"Edad cambiada a string: {edad}")
print(type(edad)) # str
print()


# ==============================
# Operadores Aritméticos
# ==============================

a = 10
b = 3

print(f"La suma es: {a + b} ")
print(f"La resta es: {a - b} ")
print(f"La multiplicacion es: {a * b} ") 
print(f"La division es: {a / b} ")
print(f"La division entera es: {a // b} ")
print(f"El modulo es: {a % b} ")
print(f"La potencia es: {a ** b} ")
print()

# Comparativos
print(f"a es igual a b: {a == b} ")
print(f"a es diferente a b: {a != b} ")
print(f"a es mayor que b: {a > b} ")
print(f"a es menor que b: {a < b} ")
print(f"a es mayor o igual que b: {a >= b} ")
print(f"a es menor o igual que b: {a <= b} ")
print()

# Operadores Lógicos

print(f"a y b son mayores que 7: {a > 7 and b > 7} ")
print(f"a o b es mayor que 7: {a > 7 or b > 7} ")
print(f"a no es mayor que b: {not a > b} ")
print()


# ==============================
# Estructuras de datos
# ==============================

# Listas (Arrays)
frutas = ["Manzana", "Banana", "Cereza"]

print("Lista de frutas: ", frutas)
print()

# Funciones para listas
frutas.append("Naranja") # Agregar un elemento al final
print("Lista de frutas despues de agregar Naranja: ", frutas)

frutas.insert(1, "Mango") # Insertar en una posicion especifica
print("Lista de frutas despues de insertar Mango en la posicion 1: ", frutas)

frutas.remove("Banana") # Eliminar un elemento
print("Lista de frutas despues de eliminar Banana: ", frutas)

frutas.pop() # Eliminar el ultimo elemento
print("Lista de frutas despues de eliminar el ultimo elemento: ", frutas)

frutas.sort() # Ordenar la lista
print("Lista de frutas ordenada: ", frutas)

frutas.reverse() # Invertir el orden de la lista
print("Lista de frutas invertida: ", frutas) 

frutas.clear() # Limpiar la lista
print("Lista de frutas despues de limpiarla: ", frutas)
print()

# Tuplas (Ordenadas pero inmutables)
colores = ("Rojo", "Verde", "Azul")
print("Tupla de colores: ", colores)

# Acceder a elementos de la tupla
print("Primer color: ", colores[0])
print("Ultimo color: ", colores[-1])
print()

# Conversion de tupla a lista
colores_lista = list(colores)
print("Tupla convertida a lista: ", colores_lista)
print()

# Conversion de lista a tupla
colores_tupla = tuple(colores_lista)
print("Lista convertida a tupla: ", colores_tupla)
print()

# Sets (Elementos unicos y desordenados, no permite duplicados)
numeros = {1, 2, 3, 4, 5}
print("Set de numeros: ", numeros)

print("Agregar un numero al set (6): ")

numeros.add(6) # Agregar un elemento    
print("Set de numeros despues de agregar 6: ", numeros)

numeros.remove(3) # Eliminar un elemento
print("Set de numeros despues de eliminar 3: ", numeros)
print()

# Diccionarios (pares clave-valor, son desordenados y mutables)
persona = {
    "nombre": "Josue",
    "apellido": "Mancia",
    "edad": 22
}
print("Diccionario persona: ", persona)

# Acceder a valores del diccionario
print("Nombre: ", persona["nombre"])
print("Apellido: ", persona.get("apellido"))
print()

# Agregar un nuevo par clave-valor  
persona["ciudad"] = "Madrid"
print("Diccionario persona despues de agregar ciudad: ", persona)

# Eliminar un par clave-valor
persona.pop("edad")
print("Diccionario persona despues de eliminar edad: ", persona)
print()

# Obtener todas las claves
print("Claves del diccionario persona: ", persona.keys())

# Obtener todos los valores
print("Valores del diccionario persona: ", persona.values())
print()

# Obtener todos los pares clave-valor
print("Pares clave-valor del diccionario persona: ", persona.items())
print()

# Limpiar el diccionario
persona.clear()
print("Diccionario persona despues de limpiarlo: ", persona)
print()


# ==================================
# Flujo de control
# ==================================

# Condicionales
edad = 18

# if
if edad < 18:
    print("Eres menor de edad")

# if-else
if edad > 18: 
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# if-elif-else
if edad < 18:
    print("Eres menor de edad")
elif edad == 18:
    print("Tienes 18 años")
else:
    print("Eres mayor de edad")
print()

# Bucles
# while
contador = 0
while contador < 5:
    print("Contador es: ", contador)
    contador += 2
print()

# for
for fruta in ["Manzana", "Banana", "Cereza"]:
    print("Fruta: ", fruta)
print()

# switch-case (Python 3.10+)
dia = 3
match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miercoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sabado")
    case 7:
        print("Domingo")
    case _:
        print("Dia no valido")
print()

# ==================================
# Funciones
# ==================================

def saludar(nombre):
    print(f"Hola, {nombre}!")
    print("Bienvenido a Python.")

nombre_usuario = "Josue"
saludar(nombre_usuario)
print()

# Función con retorno de valor
def sumar(a, b):
    return a + b    
resultado = sumar(5, 3)
print(f"La suma es: {resultado}")
print() 

# Programacion orientada a objetos (POO)
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
persona1 = Persona("Josue", 22)
persona1.presentarse()
print()
# Manejo de errores y excepciones
try:
    numero = int(input("Ingresa un numero: "))
    print(f"El numero ingresado es: {numero}")  
except ValueError:
    print("Error: Debes ingresar un numero valido.")
except Exception as e:
    print(f"Ocurrio un error inesperado: {e}")
print() 
