# início do sistema
# ...
# importando bibliotecas
import sys


print("\n\n\t\t++++++++++++++++++++++++++++++++++++++++")
print("\t\t          ** Ed$Finanças$ - v3 **                 ")
print()
# declaração de variáveis
soma = 0.0
contar_contas = 0
opcao = -1
# ...
# fazendo uso do laço de repetição while
while opcao != 0:
    # print("\x1b[2J\x1b[1;1H")
    valor = float(input("Digite o Valor da Conta ou (0 ZERO) para sair.: "))
    # print("\x1b[2J\x1b[1;1H")
    # usando a estrutura de controle
    if valor == 0:
        break
    contar_contas += 1
    soma += valor
# ...
# saída no console
print("\x1b[2J\x1b[1;1H") # limpar console
print("\n+++++++++++++++++++++++++++++++++++++++++++++ ")
print("             ++ S U M Á R I O ++                ")
print("+++++++++++++++++++++++++++++++++++++++++++++   ")
print(f"   QUANTIDADE DE CONTAS..... [ 0{contar_contas} ] ")
print(f"   TOTAL DAS CONTAS......... R$: {soma:.2f}    ")
sys.exit("\n                  Ed$Finanças$ - Obrigado!\n\n")
# fim do sistema
