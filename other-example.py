class Pessoa:
    def __init__(self, nome, idade, cor):
        self.nome = nome
        self.idade = idade
        self.cor = cor
    def name(self):
        return self.nome
    def old(self):
        return self.idade

    def cota(self):
        if self.cor == 'branca':
            return f'{self.nome} NÃO tem direito a cota'
        else:
            return f'{self.nome} TEM direito a cota'


p1 = Pessoa('Ana', 21, 'branca')
print(p1.name(), p1.old())
print(p1.cota())
p2 = Pessoa('João', 22, 'Negro')
print(p2.name(), p2.old())
print(p2.cota())

