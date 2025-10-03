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
