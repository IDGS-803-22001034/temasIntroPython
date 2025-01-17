import os

def funcion1():
    os.system('cls')
    print("Dame dos numeros: ")
    num1 = int(input("Primer número: "))
    num2 = int(input("Segundo número: "))
    print("La suma de los dos numeros es: ", num1 + num2)
    


def funcion2():
    os.system('cls')
    print("Dame dos numeros: ")
    num1 = int(input("Primer número: "))
    num2 = int(input("Segundo número: "))
    print("La resta de los dos numeros es: ", num1 - num2)

def funcion3():
    os.system('cls')
    print("Dame dos numeros: ")
    num1 = int(input("Primer número: "))
    num2 = int(input("Segundo número: "))
    print("La multiplicación de los dos numeros es: ", num1 * num2)


def funcion4():
    os.system('cls')
    print("Dame dos numeros: ")
    num1 = int(input("Primer número: "))
    num2 = int(input("Segundo número: "))
    print("La división de los dos numeros es: ", num1 / num2)



def run():
    while True:
        os.system('cls')
        print("Menú de opciones: ")
        print("1.- Suma")
        print("2.- Resta")
        print("3.- Multiplicación")
        print("4.- División")
        print("5.- Salir")
        opcion = int(input("Dame una opción: "))
        if opcion == 1:
            funcion1()
        if opcion == 2:
            funcion2()
        if opcion == 3:
            funcion3()
        if opcion == 4:
            funcion4()
        if opcion == 5:
            break
        else:
            input("Presiona la tecla enter para regresar al menú")

    


#Desde este apartado de inicia una aplicación, como si fuera main de java en netbeans
if __name__ == "__main__":
    run()