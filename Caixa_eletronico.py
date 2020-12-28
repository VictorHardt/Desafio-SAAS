from Operacoes import *

caixa_1 = Operacoes(0,0,0,0)

operacao = 1

while operacao != 0:
    
    print()
    operacao = int(input("Se você deseja fazer um depósito, digite 1. Se você deseja fazer um saque, digite 2. Se você deseja ver o saldo, digite 3. Se você deseja sair, digite 0: "))

    if operacao == 1:
        Operacoes.deposito(caixa_1)
        
    if operacao == 2:
        Operacoes.saque(caixa_1)
        
    if operacao == 3:
        Operacoes.saldo(caixa_1)
        
