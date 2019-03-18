def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = ['_' for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erro = 0

    print("A palavra é: ", (letras_acertadas))

    while(not acertou and not enforcou):

        chute = input("Qual a letra?")
        chute = chute.strip().upper()

        index = 0
        if(chute in palavra_secreta):
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index = index + 1
            print(letras_acertadas)
        else:
            erro = erro + 1

        enforcou = erro == 5
        print(letras_acertadas)

    if(acertou):
        print("Parabains. Você ganhou!")
    else:
        print("Loser faz assim mesmo kkkK")

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
