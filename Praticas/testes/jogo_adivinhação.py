import random

def adivinha_numero():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    chance = 10

    print("Bem vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número secreto entre 1 e 100")
    print(f"Você tem {chance} chances para adivinhar o número secreto")

    while tentativas < chance:
        try:
            palpite = int(input("Digite seu palpite: "))

            if palpite < 1 or palpite > 100:
                print("Número inválido! Digite um número entre 1 e 100")
                continue

            tentativas += 1

            if palpite == numero_secreto:
                print(f"Parabéns! Você acertou o número secreto em {tentativas} tentativas!")
                break

            dicas(palpite, numero_secreto)

            print(f"Você ainda tem {chance - tentativas} chances!")

        except ValueError:
            print("Digite um número válido")
            continue

    if tentativas == chance and palpite != numero_secreto:
        print(f"Suas chances acabaram! O número secreto era {numero_secreto}")

def dicas(palpite, numero_secreto):
    if palpite < numero_secreto:
        print("Tente um número maior!")
    else:
        print("Tente um número menor!")

def jogar_novamente():
    resposta = input("Deseja jogar novamente? (s/n): ").lower()

    if resposta == "s":
        adivinha_numero()
    elif resposta == "n":
        print("Obrigado por jogar!")
    else:
        print("Digite 's' para sim ou 'n' para não")

def main():
    adivinha_numero()

if __name__ == "__main__":
    main()
    
        