# início do sistema
print("\n\n\t\t++++++++++++++++++++++++++++++++++++++++")
print("\t\t          ** Ed$Finanças$ - v2 **                 ")
print()
# declaração de variáveis
soma = 0.0
contar_contas = 0
contas = int(input("Informe a Quantidade de Contas.: "))
# ...
# fazendo uso do laço de repetição for
for conta in range(contas):
    valor = float(input(f"Digite o Valor da Conta: {conta + 1}.: "))
    contar_contas = contar_contas + 1
    soma = soma + valor
# ...
# saída no console
print("\n++++++++++++++++++++++++++++++++++++++++")
print("Quantidade de Contas  ", contar_contas)
print("Soma das Contas       ", soma)
# fim do sistema
