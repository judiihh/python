continuar = "SI"
while continuar == "SI":
        print(" ")
        print("~ Calculadora del Consumo de Gasolina de su Vehículo :D ~")
        print(" ")

        print("\033[3mEn la siguiente linea, favor escribir los Galones Usados, Millas Iniciales y las Millas Finales :)\033[0m")
        print(" ")

        #GU = Galones Usados
        #MI = Millas Iniciales
        #MF = Millas Finales
        #DM = Distancia Manejada
        #MP = Millas ppg
        #DM = MF-MI
        #MP = DM/GU
        #Cuando el MP de un vehículo es mayor que 40 el vehiculo tiene un buen consumo.

        GU = float(input("-Introduzca la cantidad de Galones Usados: "))
        MI = float(input("-Introduzca la cantidad de Millas Iniciales: "))
        MF = float(input("-Introduzca la cantidad de Millas Finales: "))
        DM = MF-MI
        MP = DM/GU

        print(" ")
        print("Distancia Manejada:", MF - MI)
        print("Millas Promedio Por Galon:", DM / GU)
        print(" ")


        if MP >= 40:
                print("Su vehículo está dando un buen consumo de gasolina :)")
                
        else:
                print("Su vehículo no está dando un buen consumo de gasolina :(")
        print(" ")

        print("\033[3mSi desea continuar con otro cálculo, escriba: SI\033[0m")
        print("\033[3mSi desea terminar, escriba: NO\033[0m")
        print(" ")
        continuar =input("¿Desea realizar otro cálculo? (SI/NO): ").upper()
        if continuar == "NO":
                print(" ")
                print("Gracias por utilizar la ~ Calculadora del Consumo de Gasolina de su Vehículo :D ~. ¡Hasta luego! ")
                print(" ")