print("calculadora de 3 numeros")
print("1. sumar")
print("2. restar")
print("3. multiplicar")
print("4. dividir")

opcion = int(input("elige una opcion (1-4):"))

n1 = float(input("ingresa el primer numero:"))
n2 = float(input("ingresa el segundo numero:"))
n3 = float(input("ingresa el tercer numero:"))

if opcion == 1:
  resultado= n1 + n2 + n3
  print("la suma es:", resultado)
