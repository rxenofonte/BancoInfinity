from banco import *
from operacoes.deposito import depositar
from operacoes.consulta import consultarSaldo
from operacoes.saque import sacar
from operacoes.transferencia import transferir

def menu():
    while True:
        print("------Sistema Bancario-------")
        print("1 - Adicionar conta")
        print("2 - Editar conta")
        print("3 - Consultar conta")
        print("4 - Apagar conta")
        print("5 - Listar contas")
        print("6 - Atualizar nome")
        print("7 - Atualizar saldo")
        print("8 - Realizar saque")
        print("9 - Realizar deposito")
        print("10 - Consultar saldo")
        print("11 - Transferencia")
        print("12 - Sair")
        opcao = int(input('Selecione uma opção:'))
        if opcao == 12:
            break
menu()