"""
Tentativa:


class Motor:
    def __init__(self, velocidade=0):
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        if self.velocidade < 0:
            self.velocidade = 0


class Direcao:
    def __init__(self, valor='Norte'):
        self.valor = valor

    def girar_a_direita(self):
        if self.valor == 'Norte':
            self.valor = 'Leste'
        elif self.valor == 'Leste':
            self.valor = 'Sul'
        elif self.valor == 'Sul':
            self.valor = 'Oeste'
        elif self.valor == 'Oeste':
            self.valor = 'Norte'

    def girar_a_esquerda(self):
        if self.valor == 'Norte':
            self.valor = 'Oeste'
        elif self.valor == 'Leste':
            self.valor = 'Norte'
        elif self.valor == 'Sul':
            self.valor = 'Leste'
        elif self.valor == 'Oeste':
            self.valor = 'Sul'

    def calcular_direcao(self):
        print(self.valor)


class Carro:
    def __init__(self, direcao=Direcao(), motor=Motor()):
        self.motor = motor
        self.direcao = direcao


motor = Motor()
print(motor.velocidade)
motor.acelerar()
print(motor.velocidade)
motor.acelerar()
print(motor.velocidade)
motor.acelerar()
print(motor.velocidade)
motor.frear()
print(motor.velocidade)
motor.frear()
print(motor.velocidade)


direcao = Direcao()
print(direcao.valor)

direcao.girar_a_direita()
print(direcao.valor)

direcao.girar_a_direita()
print(direcao.valor)

direcao.girar_a_direita()
print(direcao.valor)

direcao.girar_a_direita()
print(direcao.valor)

direcao.girar_a_esquerda()
print(direcao.valor)

direcao.girar_a_esquerda()
print(direcao.valor)

direcao.girar_a_esquerda()
print(direcao.valor)

direcao.girar_a_esquerda()
print(direcao.valor)

carro = Carro(direcao, motor)
carro.calcular_velocidade()
"""
