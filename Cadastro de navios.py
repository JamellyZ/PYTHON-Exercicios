frotas = open("frotas.txt", "w")
frotas.writelines("Navio" + "\t" + "Latitude"  + "\t" + "Longitude" + "\t" + "Hora\n")
frotas.close()

def dados(navio, lat, long, hora):
    frotas = open("frotas.txt", "a")
    frotas.writelines(navio + "\t\t" + str(lat) + "\t\t" + str(long) + "\t\t" + hora + "\n")
    frotas.close()

while True:
    navio = input("Qual o tipo de navio?\n"
                  "Caso queira encerrar o programa digite 'sair'\n").lower()
    if navio == "sair":
        break
    lat = int(input("Qual a latitude em graus?\n"))
    if lat > 90:
        while lat > 90:
            lat = int(input("Valor não valido tente novamente:\n"))
    long = int(input("Qual o valor da longitude em graus?\n"))
    if long > 180:
        while long > 180:
            long = int(input("Valor não valido tente novamente:\n"))
    hora = input("Digite a hora de chegada:\n")
    dados(navio, lat, long, hora)

frotas = open("frotas.txt", "r")
ler = frotas.read()
print("Os dados adicionados são\n")
print(ler)


