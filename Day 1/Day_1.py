def numerocadena(linea):
    primero = False
    ultimo = False
    lista = list(linea)
    numero = list()
    i = 0
    j = len(lista)
    while(not (primero & ultimo)):
        if(not primero):
            pri = lista[i]
            if(pri == '1' or pri == '2' or pri == '3' or pri == '4' or pri == '5' or pri == '6' or pri == '7' or pri == '8' or pri == '9'):
                    primero = True
                    numero.insert(0,pri)
            else:
                    i = i + 1
        if(not ultimo):
            ult = lista[j-1]
            if(ult == '1' or ult == '2' or ult == '3' or ult == '4' or ult == '5' or ult == '6' or ult == '7' or ult == '8' or ult == '9'):
                ultimo = True
                numero.insert(1, ult)
            else:
                 j = j - 1
    return numero

fichero = open("input.txt")
total = 0
lineas = fichero.readlines()
for linea in lineas:
     numero = numerocadena(linea)
     num = numero[0] + numero[1]
     total = total + int(num)
print("total: "+str(total))

