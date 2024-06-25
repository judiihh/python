continuar = "SI"
while continuar == "SI":
    print(" ")
    print("~Calculadora Jud~")
    print(" ")

    print("Si deseas sumar, escribe: SUMA")
    print("Si deseas restar, escribe: RESTA")
    print("Si deseas multiplicar, escribe: MULTIPLICA")
    print("Si deseas dividir, escribe: DIVIDE")
    print(" ")

    calcular = str(input("Escribe la operación que deseas realizar: ")).upper()
    print(" ")

    if calcular == "SUMA":
        num1=float(input("Introduzca el primer valor que desea sumar: "))
        num2=float(input("Introduzca el segundo valor que desea sumar: "))
        print("Resultado:", num1 + num2)

    if calcular == "RESTA":
        num1=float(input("Introduzca el primer valor que desea restar: "))
        num2=float(input("Introduzca el segundo valor que desea restar: "))
        print("Resultado:", num1 - num2)

    if calcular == "MULTIPLICA":
        num1=float(input("Introduzca el primer valor que desea multiplicar: "))
        num2=float(input("Introduzca el segundo valor que desea multiplicar: "))
        print("Resultado:", num1 * num2)

    if calcular == "DIVIDE":
        num1=float(input("Introduzca el primer valor que desea dividir: "))
        num2=float(input("Introduzca el segundo valor que desea dividir: "))
        if num2 != 0:
            print("Resultado:", num1 / num2)
        else:
            print(" ")
            print("\033[3m*No se puede dividir entre cero. Operación no válida. Por favor, elige una opción válida.*\033[0m")
            print(" ")
            num1=float(input("Introduzca el primer valor que desea dividir: "))
            num2=float(input("Introduzca el segundo valor que desea dividir: "))
            print("Resultado:", num1 / num2)

    print(" ")
    print("Si desea continuar con otra operación, escribe: SI")
    print("Si desea terminar, escribe: NO")
    print(" ")
    continuar =input("¿Deseas realizar otra operación? (SI/NO): ").upper()
    if continuar == "NO":
        print(" ")
        print("Gracias por utilizar la ~Calculadora Jud~. ¡Hasta luego! ")
        print(" ")