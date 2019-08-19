agenda = open("contatos.txt", "w")
agenda.write("Nome" + "\t" + "Telefone\n")
agenda.close()

sair = ""

def add(nome, telefone):
    agenda = open("contatos.txt", "a")
    agenda.writelines(nome + "\t" + telefone + "\n")
    agenda.close()

while sair != "sair":
    name = input("Digite um nome para colocar na agenda\n")
    numero = input("Agora digite o número\n")
    sair = input("Caso queira encerrar o programa digite 'sair', caso contrario aperte a tecla ENTER do seu teclado\n").lower()
    add(name,numero)
