def ordem(n1,n2,n3):
    lista = []
    lista.append(n1)
    lista.append(n2)
    lista.append(n3)
    lista.sort()
    print("Os números ordenados são:", lista)

n1 = int(input("Digite um número:\n"))
n2 = int(input("Digite outro número:\n"))
n3 = int(input("Digite mais um:\n"))
ordem(n1,n2,n3)