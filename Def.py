class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar(self):
        print(f"Meu nome é {self.nome} e tenho {self.idade} anos.")

p1 = Pessoa("Ana", 3)
p2 = Pessoa("Luiz", 18)

p1.mostrar()
p2.mostrar()

#####################################################################################################################
