
class OperasBas:
    #declaración de propiedades
    #_ es para privado,publico no lleva nada y para protegido es __ 
    num1=0
    num2=0
    res=0
    #declaración de constructor de la clase, inicializar los atributos de la clase
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    #declaración de métodos de la clase
    def suma(self):
        self.res=self.num1+self.num2
        print("La suma es:{}".format(self.res))

def main():
    obj=OperasBas(3,5)
    obj.suma()

if __name__=="__main__":
    main()