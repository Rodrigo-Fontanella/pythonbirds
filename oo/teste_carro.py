from unittest import TestCase

from oo.carro import Motor

class CarroTesteCase(TestCase):
    def teste_velocidade_inicial(self): #Para rodar o test, sempre comece com o prefixo 'test'
        motor = Motor()
        self.assertEqual(0, motor.velocidade) #fez um teste comparando a velocidade inicial do Motor, que é 0

    def teste_acelerar(self):
        motor = Motor()
        motor.acelerar()
        self.assertEqual(1, motor.velocidade)
