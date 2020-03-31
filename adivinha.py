total_rodadas = 3
rodada_atual = 1
numero_secreto = 42

print("Bem-vindo ao jogo de adivinhação")

while (rodada_atual <= total_rodadas):
    print("Você terá ", total_rodadas, "chances, e essa é sua ", rodada_atual, "ª rodada. Boa sorte!")
   
    chute_str = input("Digite seu chute: ")
    
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto
    rodada_atual = rodada_atual + 11   

    if (acertou):
        print("Parabéns, você acertou")
    else:
        if (maior):
            print("Que pena, você chutou um número maior!")
        elif (menor):
            print("Que pena, você chutou um número menor!")



print("Fim do jogo!")
