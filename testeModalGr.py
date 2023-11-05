# Função para calcular as notas necessárias
def calcular_notas(valor):
    notas_de_maior_valor = []
    notas_de_menor_valor = []

    # Verifica se o valor é múltiplo de 2
    if valor % 2 != 0:
        return "Insira um valor válido!"

    # Notas de maior valor (100 e 50 reais)
    while valor >= 100:
        notas_de_maior_valor.append(100)
        valor -= 100
    while valor >= 50:
        notas_de_maior_valor.append(50)
        valor -= 50

    # Notas de menor valor (20, 10, 5 e 2 reais)
    while valor >= 20:
        notas_de_menor_valor.append(20)
        valor -= 20
    while valor >= 10:
        notas_de_menor_valor.append(10)
        valor -= 10
    while valor >= 5:
        notas_de_menor_valor.append(5)
        valor -= 5
    while valor >= 2:
        notas_de_menor_valor.append(2)
        valor -= 2

    return notas_de_maior_valor, notas_de_menor_valor

# Função para exibir as opções de retirada
def exibir_opcoes_retirada(notas_maior_valor, notas_menor_valor):
    print("Notas de maior valor:")
    for nota in notas_maior_valor:
        print(f"➢ {nota} x 100 reais" if nota == 100 else f"➢ {nota} x 50 reais")

    print("\nNotas de menor valor:")
    for nota in notas_menor_valor:
        print(f"➢ {nota} x 20 reais" if nota == 20 else f"➢ {nota} x 10 reais" if nota == 10 else f"➢ {nota} x 5 reais" if nota == 5 else f"➢ {nota} x 2 reais")

# Solicitar informações do colaborador
nome = input("Digite o nome do colaborador: ")
data_admissao = input("Digite a data de admissão (no formato DD/MM/AAAA): ")
salario_atual = float(input("Digite o salário atual: R$ "))
valor_emprestimo = float(input("Digite o valor de empréstimo: R$ "))

# Verificar se o colaborador atende aos requisitos mínimos
anos_na_empresa = 2023 - int(data_admissao.split("/")[2])
if anos_na_empresa <= 5:
    print("Agradecemos seu interesse, mas você não atende os requisitos mínimos do programa.")
else:
    notas_maior_valor, notas_menor_valor = calcular_notas(valor_emprestimo)
    if notas_maior_valor == "Insira um valor válido!":
        print(notas_maior_valor)
    else:
        print(f"Valor empréstimo: {int(valor_emprestimo)} reais")
        exibir_opcoes_retirada(notas_maior_valor, notas_menor_valor)
