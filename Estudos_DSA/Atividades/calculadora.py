# Importando o módulo math para funções matemáticas avançadas
import math

class Calculadora:
    def __init__(self):
        # Dicionário que mapeia os símbolos das operações para seus respectivos métodos
        # Isso permite chamar as funções de forma dinâmica baseado na entrada do usuário
        self.operacoes = {
            '+': self.soma,
            '-': self.subtracao,
            '*': self.multiplicacao,
            '/': self.divisao,
            '^': self.potencia,
            'sqrt': self.raiz_quadrada,
            'log': self.logaritmo,
            'sin': self.seno,
            'cos': self.cosseno,
            'tan': self.tangente,
            '%': self.porcentagem
        }
    
    def exibir_menu(self):
        """Exibe o menu principal da calculadora com todas as operações disponíveis"""
        print("=" * 40)
        print("Calculadora Avançada")
        print("=" * 40)
        print("Operações disponíveis:")
        print("1. Soma (+)")
        print("2. Subtração (-)")
        print("3. Multiplicação (*)")
        print("4. Divisão (/)")
        print("5. Potência (^)")
        print("6. Raiz Quadrada (sqrt)")
        print("7. Logaritmo Natural (log)")
        print("8. Seno (sin)")
        print("9. Cosseno (cos)")
        print("10. Tangente (tan)")
        print("11. Porcentagem (%)")
        print("=" * 40)

    # Métodos básicos de operação
    def soma(self, a, b):
        """Realiza a soma de dois números"""
        return a + b

    def subtracao(self, a, b):
        """Realiza a subtração de dois números"""
        return a - b

    def multiplicacao(self, a, b):
        """Realiza a multiplicação de dois números"""
        return a * b

    def divisao(self, a, b):
        """Realiza a divisão de dois números com verificação de divisão por zero"""
        if b == 0:
            return "Erro: Não é possível dividir por zero!"
        return a / b

    # Métodos de operações avançadas
    def potencia(self, a, b):
        """Calcula a potência de um número elevado a outro"""
        return a ** b

    def raiz_quadrada(self, a, b=None):
        """Calcula a raiz quadrada de um número com verificação de número negativo"""
        if a < 0:
            return "Erro: Não é possível calcular raiz quadrada de número negativo!"
        return math.sqrt(a)

    def logaritmo(self, a, b=None):
        """Calcula o logaritmo natural de um número com verificação de número válido"""
        if a <= 0:
            return "Erro: Não é possível calcular logaritmo de número negativo ou zero!"
        return math.log(a)

    # Métodos de funções trigonométricas (convertendo graus para radianos)
    def seno(self, a, b=None):
        """Calcula o seno de um ângulo em graus"""
        return math.sin(math.radians(a))

    def cosseno(self, a, b=None):
        """Calcula o cosseno de um ângulo em graus"""
        return math.cos(math.radians(a))

    def tangente(self, a, b=None):
        """Calcula a tangente de um ângulo em graus"""
        return math.tan(math.radians(a))

    def porcentagem(self, a, b):
        """Calcula a porcentagem de um número em relação a outro"""
        return (a * b) / 100

    def calcular(self, num1, num2, operacao):
        """
        Executa a operação matemática selecionada
        Verifica se a operação existe e se precisa de um ou dois números
        """
        if operacao in self.operacoes:
            # Para operações que precisam de apenas um número
            if operacao in ['sqrt', 'log', 'sin', 'cos', 'tan']:
                return self.operacoes[operacao](num1)
            return self.operacoes[operacao](num1, num2)
        return "Operação inválida!"

    def executar(self):
        """
        Método principal que executa a calculadora
        Gerencia o loop principal e a interação com o usuário
        """
        self.exibir_menu()
        
        while True:
            try:
                # Obtendo a operação primeiro para saber se precisa de um ou dois números
                operacao = input("Digite a operação desejada (+, -, *, /, ^, sqrt, log, sin, cos, tan, %): ")
                
                # Obtendo os números baseado no tipo de operação
                if operacao in ['sqrt', 'log', 'sin', 'cos', 'tan']:
                    num1 = float(input("Digite o número: "))
                    num2 = None
                else:
                    num1 = float(input("Digite o primeiro número: "))
                    num2 = float(input("Digite o segundo número: "))

                # Realizando a operação escolhida
                resultado = self.calcular(num1, num2, operacao)
                
                # Formatando a saída de acordo com o tipo de operação
                if operacao in ['sqrt', 'log', 'sin', 'cos', 'tan']:
                    print(f"Resultado: {operacao}({num1}) = {resultado}")
                elif operacao == '%':
                    print(f"Resultado: {num1}% de {num2} = {resultado}")
                else:
                    print(f"Resultado: {num1} {operacao} {num2} = {resultado}")

                # Perguntando se o usuário quer continuar
                continuar = input("\nDeseja fazer outro cálculo? (s/n): ")
                if continuar.lower() != 's':
                    print("Obrigado por usar a calculadora!")
                    break

            except ValueError:
                print("Erro: Por favor, digite números válidos!")
            except Exception as e:
                print(f"Ocorreu um erro: {e}")

# Execução principal do programa
if __name__ == "__main__":
    # Criando uma instância da calculadora e iniciando sua execução
    calc = Calculadora()
    calc.executar() 