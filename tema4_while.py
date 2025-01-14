


print("Dame un número")
numU=input('Número:')
x=0
print("Su tabla de multiplicar es la siguiente:")
while x<10:
    x=x+1
    result=int(numU)*int(x)
    print("{} x {} = {}".format(numU,x,result))