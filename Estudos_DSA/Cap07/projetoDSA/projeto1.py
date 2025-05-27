# Import
import random
from os import system, name # os é uma biblioteca que contém funções para interagir com o sistema operacional

# Função para limpar a tela a cada execução
def limpa_tela():

    # Windows
    if name == 'nt':
        _ = system('cls')

    # Mac ou Linux
    else:
        _ = system('clear')

# Função
def game():

    limpa_tela()
    print("\nBem-vindo(a) ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")

    # Lista de palavras para o jogo
    palavras = ['banana', 'abacate', 'uva', 'morango','laranja']

    # Escolhe randomicamente uma palavra
    palavra = random.choice(palavras) # choice é uma função que escolhe um elemento aleatório de uma lista

    # List comprehension
    letras_descobertas = ['_' for letra in palavra]

    # Número de chances
    chances = 6

    # Lista para as letras erradas
    letras_erradas = []

    # loop  enquanto número de chances for maior do que zero
    while chances > 0:
        # Print
        print(" ".join(letras_descobertas)) # join é uma função que junta os elementos de uma lista em uma string
        print("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(letras_erradas))

        # Tentativa
        tentativa = input("\nDigite uma letra: ").lower()

        # Condicional
        if tentativa in palavra:
            index = 0 # index é uma variável que armazena o índice da letra na palavra

            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra # substitui o '_' pela letra correta
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        # Condicional
        if "_" not in letras_descobertas:
            print("\nVocê venceu, a palavra era: ", palavra)
            break

    # Condicional
    if "_" in letras_descobertas:
        print("\nVocê perdeu, a palavra era: ", palavra)

# Bloco main
if __name__ == "__main__":
    game()
    print("\nParabéns. Você está aprendendo programação em Python com a DSA. :)\n")