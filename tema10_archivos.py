from io import open

texto="una line nueva con a"
archivo=open("archivo.txt","a")
archivo.write(texto)

archivo.close()