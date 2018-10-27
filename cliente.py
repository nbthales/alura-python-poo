class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    # esse metodo representa uma propriedade
    # não precisa de () mais.
    @property
    def nome(self):
        print(f'Chamando @property nome()')
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print(f'Chamando setter nome()')
        self.__nome = nome
