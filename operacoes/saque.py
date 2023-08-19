from banco import obterConta

def sacar(conta:int,valor:float) -> bool:
    cliente = obterConta(conta)
    if cliente:
        if cliente['saldo'] >= valor:
            cliente['saldo'] -= valor
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente!")
    else:
        print("Cliente não encontrado!")
