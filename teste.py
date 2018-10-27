def cria_conta(numero, titular, saldo, limite):
    conta = {'numero': numero, 'titular': titular, 'saldo': saldo, 'limite': limite}
    return conta


def deposita(conta, valor):
    conta['saldo'] += valor


def saca(conta, valor):
    conta['saldo'] -= valor


def extrato(conta):
    print(f'Saldo é {conta["saldo"]}')

# COMANDOS NO CONSOLE
# from conta import Conta
# conta = Conta(123, 'Thales', 55.5, 1000.0)
# conta2 = Conta(321, 'Marco', 100.0, 1000.0)
## transferindo da conta para a conta2
# conta.transfere(10.0, conta2)
