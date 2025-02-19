import math

def tamanho_vetor(vetor):
    return math.sqrt(vetor[0]**2 + vetor[1]**2 + vetor[2]**2)

def normalizar_vetor(vetor):
    tamanho = tamanho_vetor(vetor)
    try:
        return [vetor[0]/tamanho, vetor[1]/tamanho, vetor[2]/tamanho]
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero.")
        return vetor

def adicionar_vetores(vetor1, vetor2):
    return [vetor1[0] + vetor2[0], vetor1[1] + vetor2[1], vetor1[2] + vetor2[2]]

def subtrair_vetores(vetor1, vetor2):
    return [vetor1[0] - vetor2[0], vetor1[1] - vetor2[1], vetor1[2] - vetor2[2]]

def multiplicar_vetor_escalar(vetor, escalar):
    return [vetor[0] * escalar, vetor[1] * escalar, vetor[2] * escalar]

def dividir_vetor_escalar(vetor, escalar):
    try:
        return [vetor[0] / escalar, vetor[1] / escalar, vetor[2] / escalar]
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero.")
        return vetor

def produto_escalar(vetor1, vetor2):
    return vetor1[0] * vetor2[0] + vetor1[1] * vetor2[1] + vetor1[2] * vetor2[2]

def ler_vetor():
    x = float(input("Digite o valor de x: "))
    y = float(input("Digite o valor de y: "))
    z = float(input("Digite o valor de z: "))
    return [x, y, z]

def exibir_menu():
    print("\nEscolha uma opção:")
    print("a) Calcular o tamanho do vetor")
    print("b) Normalizar o vetor")
    print("c) Adicionar outro vetor")
    print("d) Subtrair outro vetor")
    print("e) Multiplicar o vetor por um escalar")
    print("f) Dividir o vetor por um escalar")
    print("g) Calcular o produto escalar com outro vetor")
    print("h) Sair")

def main():
    print("Digite os valores do vetor inicial (x, y, z):")
    vetor = ler_vetor()

    while True:
        exibir_menu()
        escolha = input("Digite a opção desejada: ").lower()

        if escolha == 'a':
            print(f"Tamanho do vetor: {tamanho_vetor(vetor):.2f}")
        elif escolha == 'b':
            vetor_normalizado = normalizar_vetor(vetor)
            print(f"Vetor normalizado: {vetor_normalizado}")
        elif escolha == 'c':
            print("Digite os valores do vetor a ser adicionado (x, y, z):")
            vetor_adicional = ler_vetor()
            vetor = adicionar_vetores(vetor, vetor_adicional)
            print(f"Vetor resultante após adição: {vetor}")
        elif escolha == 'd':
            print("Digite os valores do vetor a ser subtraído (x, y, z):")
            vetor_subtraido = ler_vetor()
            vetor = subtrair_vetores(vetor, vetor_subtraido)
            print(f"Vetor resultante após subtração: {vetor}")
        elif escolha == 'e':
            escalar = float(input("Digite o valor do escalar: "))
            vetor_multiplicado = multiplicar_vetor_escalar(vetor, escalar)
            print(f"Vetor resultante após multiplicação: {vetor_multiplicado}")
        elif escolha == 'f':
          
            escalar = float(input("Digite o valor do escalar: "))
            vetor_dividido = dividir_vetor_escalar(vetor, escalar)
            print(f"Vetor resultante após divisão: {vetor_dividido}")
        elif escolha == 'g':
            print("Digite os valores do outro vetor (x, y, z):")
            vetor_produto = ler_vetor()
            resultado_produto = produto_escalar(vetor, vetor_produto)
            print(f"Produto escalar: {resultado_produto}")
        elif escolha == 'h':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
