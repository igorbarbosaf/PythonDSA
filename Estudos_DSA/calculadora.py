def calculadora():
    # Função principal que executa a calculadora
    print("=" * 30)
    print("Calculadora Simples")
    print("=" * 30)
    print("Operações disponíveis:")
    print("1. Soma (+)")
    print("2. Subtração (-)")
    print("3. Multiplicação (*)")
    print("4. Divisão (/)")
    print("=" * 30)

def soma(a, b):
    # Função para realizar a soma
    return a + b

def subtracao(a, b):
    # Função para realizar a subtração
    return a - b

def multiplicacao(a, b):
    # Função para realizar a multiplicação
    return a * b

def divisao(a, b):
    # Função para realizar a divisão com tratamento de erro
    if b == 0:
        return "Erro: Não é possível dividir por zero!"
    return a / b

# Execução principal do programa
if __name__ == "__main__":
    calculadora()

    while True:
        try:
            # Obtendo os números e a operação do usuário
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            operacao = input("Digite a operação desejada (+, -, *, /): ")

            # Realizando a operação escolhida
            if operacao == "+":
                resultado = soma(num1, num2)
                print(f"Resultado: {num1} + {num2} = {resultado}")
            elif operacao == "-":
                resultado = subtracao(num1, num2)
                print(f"Resultado: {num1} - {num2} = {resultado}")
            elif operacao == "*":
                resultado = multiplicacao(num1, num2)
                print(f"Resultado: {num1} * {num2} = {resultado}")
            elif operacao == "/":
                resultado = divisao(num1, num2)
                print(f"Resultado: {num1} / {num2} = {resultado}")
            else:
                print("Operação inválida!")

            # Perguntando se o usuário quer continuar
            continuar = input("\nDeseja fazer outro cálculo? (s/n): ")
            if continuar.lower() != 's':
                print("Obrigado por usar a calculadora!")
                break

        except ValueError:
            print("Erro: Por favor, digite números válidos!")
        except Exception as e:
            print(f"Ocorreu um erro: {e}") 