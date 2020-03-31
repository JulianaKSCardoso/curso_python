total_rodadas = 3
rodada_atual = 1
numero_secreto = 42

print("Bem-vindo ao jogo de adivinhação")

while (rodada_atual <= total_rodadas):
    print("Você terá {} chances, e essa é sua {}ª rodada. Boa sorte!" .format(total_rodadas, rodada_atual))
   
    chute_str = input("Digite seu chute: ")

    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    rodada_atual = rodada_atual + 1   

    if (acertou):
        print("Parabéns, você acertou")
    else:
        if (maior):
            print("Que pena, você chutou um número maior!")
        elif (menor):
            print("Que pena, você chutou um número menor!")



print("Fim do jogo!")
