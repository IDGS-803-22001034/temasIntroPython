from io import open
import os

class Diccionario:
    palabraE=[]
    palabraI=[]

    def __init__(self):
        self.cargar_datos_todos()


    def cargar_datos_todos(self):
        if os.path.exists("Diccionario.txt"):
            with open("Diccionario.txt", "r") as archivo:
                for linea in archivo:
                    if ':' in linea:
                        esp, ing = linea.strip().split(':')
                        self.palabraE.append(esp)
                        self.palabraI.append(ing)

                        
    def buscar(self):
            os.system('cls')
            print("1.- Español")
            print("2.- Ingles")
            opcion = int(input("Dame una opción: "))
            if opcion == 1:
                palabra = input("Dame la palabra en español: ")
                if palabra in self.palabraE:
                    pocision = self.palabraE.index(palabra)
                    print(f"Palabra encontrada: {self.palabraI[pocision]}")
                else:
                    print("Palabra no encontrada en el diccionario.")
            elif opcion == 2:
                palabra = input("Dame la palabra en inglés: ")
                if palabra in self.palabraI:
                    pocision = self.palabraI.index(palabra)
                    print(f"Palabra encontrada: {self.palabraE[pocision]}")
                else:
                    print("Palabra no encontrada.")
            else:
                print("Palabra no encontrada")



    
            
            
    def captura(self):
        os.system('cls')
        palabraE = input("Palabra en Español:")
        palabraI = input("Palabra en Ingles:")
        archivo=open("Diccionario.txt","a")
        archivo.write("\n{}:{}".format(palabraE,palabraI))
        self.palabraE.append(palabraE)
        self.palabraI.append(palabraI)
        
            


def main():
   obj=Diccionario()
   while True:
            os.system('cls')
            print("Menú de opciones: ")
            print("1.- Capturar palabras")
            print("2.- Buscar palabras")
            print("3.- Salir")
            opcion = int(input("Dame una opción: "))
            if opcion == 1:
                obj.captura()
            if opcion == 2:
                obj.buscar()
            if opcion == 3:
                break
            else:
                input("Presiona la tecla enter para regresar al menú")



if __name__=="__main__":
    main()