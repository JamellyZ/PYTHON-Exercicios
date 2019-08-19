def tabuada(n1):
    cont = 1
    while cont != 11:
        print(n1, "X",cont, "=", (cont*n1))
        cont+=1

n1 = int(input("Digite um número para saber sua tabuada\n"))
tabuada(n1)