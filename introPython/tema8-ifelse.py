print("Suma de numeros: ")
num1 = int(input("Dame un numero 1"))
num2 = int(input("Dame un numero 2"))

print("La suma es: {} + {} = {}".format(num1, num2, num1 + num2))

if num1 > num2:
    print("El {} es mayor que el {}".format(num1, num2))
else:
    print("El {} es mayor que el {}".format(num2, num1))

pint("---------------------------Pedir una edad -----------------")
edad = int(input("Ingresar tu edad "))
if edad > 18:
    print("Eres mayor de edad")
elif edad == 18:
    print(" No Eres mayor de edad")
else:
    print("Eres menor de edad")


