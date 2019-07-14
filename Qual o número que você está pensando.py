from random import  *
numero_aleatorio = randrange(2, 20, 2)

def checar(opcao):
    if opcao == "ok":
        pass
    else:
        while opcao != "ok":
            opcao = input("Opcão invalida digite 'ok' para proseguir:")


resultado = ""
print("Bem vindo ao jogo do adivinhando o pensamento, serão feitos alguns pedidos a você e no fim tentaremos adivinhar o número que você está pensando\n")
while resultado != "2":
    numero = input("PENSE EM UM NÚMERO:\n"
                   "Digite 'ok' caso tenho já tenha pensado:\n").lower()
    checar(numero)

    dobro = input("PENSE NO DOBRO DO NÚMERO QUE VOCÊ PENSOU:\n"
                  "Digite 'ok' caso já tenha pensado no dobro:\n").lower()
    checar(dobro)

    adicione = input(f"AGORA ADICIONE MAIS {numero_aleatorio} \n"
                    "Digite 'ok' caso tenha adicionado o número:\n").lower()

    checar(adicione)

    dividir = input("AGORA DIVIDA NO MEIO\n"
                    "Digite 'ok' caso já tenha dividido no meio o número pensado\n").lower()

    checar(dividir)

    subtrair = input("AGORA SUBTRAIA PELO NÚMERO QUE VOCÊ PENSOU NO INICIO\n"
                     "Digite 'ok' caso já tenha subtraido:\n").lower()

    checar(subtrair)

    resultado = input(f"O resultado que você está pensando agora é {numero_aleatorio/2}:\n"
                      "Digite 1- Caso queira jogar novamente\n"
                      "Digite 2 - Caso queira sair\n")


