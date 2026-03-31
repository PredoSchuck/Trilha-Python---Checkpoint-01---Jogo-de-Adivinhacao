import random

tentativas = 0
secreto = random.randint(1, 100)
descobrir = 0

while True:
    descobrir = int(input("Digite um número entre 0 e 100"))
    
    if descobrir < 1 or descobrir > 100:
        print("Digite um número válido!")
    elif descobrir == secreto:
        print(f"Parabéns, você acertou com {tentativas} tentativas")
        break
    else:
        descobrir = int(input(f"Você errou, restam {tentativas}, tente novamente! "))

    #     tentativas += 1
