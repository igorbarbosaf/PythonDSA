# Projeto 1 - Desenvolvimento de Game em Linguagem Python - Versão 2

# Import
import random
from os import system, name

# Função para limpar a tela a cada execução
def limpar_tela():
    # Para windows
    if name == 'nt':
        _ = system('cls')
    # Para mac e linux
    else:
        _ = system('clear')

# função que desenha a forca na tela
def display_hangman(chances):
    # Lista de estágios da forca
    stages = [ # estágio 6 (final)
        """
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |     / \\
        |
        --------
        """,
        # estágio 5
        """
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |     /
        |
        --------
        """,
        # estágio 4
        """
        --------
        |      |
        |      O
        |     \\|/
        |      |
        |
        --------
        """,
        # estágio 3
        """
        --------
        |      |
        |      O
        |     \\|
        |      |
        |
        --------
        """,
        # estágio 2
        """
        --------
        |      |
        |      O
        |      |
        |      |
        |
        --------
        """,
        # estágio 1
        """
        --------
        |      |
        |      O
        """,
        # estágio 0 (início)
        """
        --------
        |      |
        |      
        """,
    ]
    return stages[chances]

# Função do jogo
def game():
    limpar_tela()
    print("\nBem-vindo ao jogo da forca!")
    print("Adivinhe a palavra abaixo:")

    # Lista de Palavras para o jogo
    palavras = ['maçã', 'tangerina', 'kiwe', 'morango', 'pera']

    # Escolhe randomicamente uma palavra
    palavra_secreta = random.choice(palavras)

    # Lista de letras da palavra
    lista_letras_palavra = [letra for letra in palavra_secreta]

    # Cria o tabuleiro com caracter "_" multiplicado pelo comprimento da palavra
    tabuleiro = ["_"] * len(palavra_secreta)

    # Número de chances
    chances = 6

    # Lista para as letras digitadas
    letras_tentativas = []

    # Loop enquanto número de chances for maior do que zero
    while chances > 0:
        print(display_hangman(chances))
        print("Palavra: ", tabuleiro)
        print("\n")

        # Tentativa
        tentativa = input("\nDigite uma letra: ").lower()

        # Condicional
        if tentativa in letras_tentativas:
            print("Você já tentou essa letra. Escolha outra!")
            continue

        # Lista de tentativas (letras)
        letras_tentativas.append(tentativa)

        # Condicional
        if tentativa in lista_letras_palavra:
            print("Você acertou a letra!")

            # Loop
            for indice in range(len(lista_letras_palavra)):
                # Condicional
                if lista_letras_palavra[indice] == tentativa:
                    tabuleiro[indice] = tentativa

            # Se todos os espaços foram preenchidos, o jogo acabou
            if "_" not in tabuleiro:
                print("\nVocê venceu! A palavra era: {}".format(palavra_secreta))
                break

        else:
            print("Ops. Essa letra não está na palavra!")
            # Decremento(Diminuição)
            chances -= 1

    # Condicional
    if "_" in tabuleiro:
        print("\nVocê perdeu! A palavra era: {}".format(palavra_secreta))

# Bloco main
if __name__ == "__main__":
    game()