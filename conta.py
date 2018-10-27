
class Conta:
    def __init__(self, numero, titular, saldo, limite):
        # __init__ função construtora
        # self é a referência que sabe encontrar o obj
        print(f'Construindo objeto... {self}')
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
