# Função para soma
def soma(x, y):
    return x + y

# Função para subtração
def subtracao(x, y):
    return x - y

# Função para multiplicação
def multiplicacao(x, y):
    return x * y

# Função para divisão
def divisao(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro! Divisão por zero."

# Função principal para menu
def menu():
    print("Selecione uma operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

# Loop para interação com o usuário
while True:
    menu()
    escolha = input("Escolha a operação (1/2/3/4) ou 'sair' para encerrar: ")

    if escolha == 'sair':
        print("Saindo...")
        break

    if escolha in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print(f"{num1} + {num2} = {soma(num1, num2)}")
        elif escolha == '2':
            print(f"{num1} - {num2} = {subtracao(num1, num2)}")
        elif escolha == '3':
            print(f"{num1} * {num2} = {multiplicacao(num1, num2)}")
        elif escolha == '4':
            print(f"{num1} / {num2} = {divisao(num1, num2)}")
    else:
        print("Opção inválida! Tente novamente.")
