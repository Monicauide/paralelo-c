"""nombre = input("Por favor, ingresa tu nombre: ")
nombre1 = input("ingrese un numero")
print ("5")
print ("hola mundo")
print ("universidad internacional del ecuador")"""

"""# 1. Operador Igual que (==)
a = 10
b = 15
print("¿a es igual a b?", a == b)  # False

# 2. Operador Distinto de (!=)
print("¿a es distinto de b?", a != b)  # True

# 3. Operador Mayor que (>)
print("¿a es mayor que b?", a > b)  # False

# 4. Operador Menor que (<)
print("¿a es menor que b?", a < b)  # True

# 5. Operador Mayor o igual que (>=)
c = 10
print("¿a es mayor o igual que c?", a >= c)  # True

#ejercicio en clase

# Solicitar al usuario dos números
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# Comparaciones
print("¿El primer número es igual al segundo?", num1 == num2)
print("¿El primer número es distinto del segundo?", num1 != num2)
print("¿El primer número es mayor que el segundo?", num1 > num2)
print("¿El primer número es menor que el segundo?", num1 < num2)
print("¿El primer número es mayor o igual que el segundo?", num1 >= num2)
print("¿El primer número es menor o igual que el segundo?", num1 <= num2)
"""

"""#operadores logicos

# Operadores lógicos: ejemplos básicos
a = True
b = False

# AND: Ambas condiciones deben ser verdaderas
print("a AND b:", a and b)  # False

# OR: Al menos una condición debe ser verdadera
print("a OR b:", a or b)  # True

# NOT: Invierte el valor de la condición
print("NOT a:", not a)  # False
print("NOT b:", not b)  # True"""





"""#Ejercicio en clase

# Valores para comparar
edad = int(input("Ingresa tu edad: "))
ingresos = float(input("Ingresa tus ingresos mensuales: "))

# Condiciones combinadas con operadores lógicos
es_adulto = edad >= 18
tiene_buen_ingreso = ingresos > 3000

# Evaluar si cumple ambas condiciones
#print("\nResultados:")
print("¿Eres adulto Y tienes buen ingreso? (AND):", es_adulto and tiene_buen_ingreso)
print("¿Eres adulto O tienes buen ingreso? (OR):", es_adulto or tiene_buen_ingreso)
print("¿No eres adulto? (NOT):", not es_adulto)"""  

#condicionales
#ejercicio 1
# Ejercicio 1: Verificar si un número es positivo
numero = int(input("Ingresa un número: "))

if numero > 0:
    print("El número es positivo.")




#condicionales
#ejercicio 2
x = 10
if x > 5:
    print("x es mayor que 5")
elif x == 5:
    print("x es igual a 5")

else:
    print("x es menor que 5")



#ejercicio No. 2
5 == 5  # True
5 == 3  # False


#ejercicio No. 3

# Ejercicio 3: Verificar si un número es positivo o negativo
numero = int(input("Ingresa un número: "))

if numero > 0:
    print("El número es positivo.")
else:
    print("El número es negativo o cero.")


#ejercicio No. 4
# Ejercicio 3: Clasificar la edad de una persona
edad = int(input("Ingresa tu edad: "))

if edad < 18:
    print("Eres menor de edad.")
elif edad >= 18 and edad <= 65:
    print("Eres un adulto.")
else:
    print("Eres un adulto mayor.")


    #ejercicio No. 5

    # Ejercicio 6: Asignar una calificación según la nota
nota = float(input("Ingresa tu nota (0-10): "))

if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Aprobado")
elif nota >= 5:
    print("Necesita mejorar")
else:
    print("Reprobado")

    #Ejercicio 7

    # Ejercicio 7: Menú de opciones
print("Menú de opciones:")
print("1. Saludar")
print("2. Despedirse")
print("3. Salir")

opcion = int(input("Selecciona una opción (1-3): "))

if opcion == 1:
    print("¡Hola! ¿Cómo estás?")
elif opcion == 2:
    print("¡Adiós! Que tengas un buen día.")
elif opcion == 3:
    print("Saliendo del programa...")
else:
    print("Opción no válida.")