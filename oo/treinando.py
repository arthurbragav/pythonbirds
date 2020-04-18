class Mulheres:
    def __init__(self, nome, cabelo, altura):
        self.nome = nome
        self.cabelo = cabelo
        self.altura = altura

    def exibeinfo(self):
        print(self.nome, self.cabelo, self.altura)


mulher1 = Mulheres('Gabi', 'Preto', '1,65')
mulher1.exibeinfo()
print(mulher1.nome)



