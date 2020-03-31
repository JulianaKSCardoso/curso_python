print("Bem-vindo ao jogo de adivinhação")

numero_secreto = 42

chute_str = input("Digite seu chute: ")
chute = int(chute_str)

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if (acertou):
    print("Parabéns, você acertou")
else:
    if (maior):
        print("Que pena, você chutou um número maior!")
    elif (menor):
        print("Que pena, você chutou um número menor!")

print("Fim do jogo!")