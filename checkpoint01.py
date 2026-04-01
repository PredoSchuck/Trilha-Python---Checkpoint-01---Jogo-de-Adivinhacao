import random

tentativas = 7
secreto = random.randint(1, 100)
descobrir = 0

while True:
    descobrir = int(input(f"Digite um número entre 0 e 100: "))
    tentativas -= 1
    if descobrir < 1 or descobrir > 100:
        print("Digite um número válido!")
    elif descobrir == secreto:
        print(f"Parabéns! você acertou com {tentativas} tentativas restantes!")
        break
    elif secreto < descobrir:
        print(f"Você errou, restam {tentativas}, tente novamente!\nDica: o número é menor ")
    elif secreto > descobrir:
        print(f"Você errou, restam {tentativas}, tente novamente!\nDica: o número é maior ")