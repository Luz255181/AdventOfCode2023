def valido(line):
    games = line.split(";")
    azul = 0
    rojo = 0
    verde = 0
    valido = False
    for game in games:
        jugadas = game.split(",")
        for i in range(len(jugadas)):
            jugada = jugadas[i].split(" ")
            match jugada[2]:
                case "red":
                    rojo = rojo + int(jugada[1])
                case "blue":
                    azul = azul + int(jugada[1])
                case "green":
                    verde = verde + int(jugada[1])
    if (rojo <= 12 and azul <= 14 and verde <= 13):
        valido = True
    return(valido)


fichero = open("input.txt")
total = 0
lineas = fichero.readlines()
for linea in lineas:
     game = linea.split(":")
     numbergame = game[0].split(" ")
     if(valido(game[1])):
          total = total + int(numbergame[1])
          print("total parcial:" + str(total))
print("total: "+str(total))