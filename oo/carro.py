"""
Você deve criar uma classe carro que vai poossuir 2 atributos compostos por outras 2 classes:

1)Motor
2)Direção

O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade
2) Método acelerar, que deverá incrementar a velocidade de uma unidade
3) Método frear que deverá decrementar a velocidade em 2 unidades

A Direção terá a responsabilidade de controlar a direção. Ela oferece os seguintes atributos:
1) Valor direção com valores possíveis: Norte, Sul, Leste, Oeste
2) Método girar_a_direita
2) Método girar_a_esquerda

   N
O     L
   S

    Exemplo:
    #Testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3

    >>> motor.frear()
    >>> motor.velocidade
    0

    #testando Direção
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'

    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>>carro.calculat_velocidade()
    1
    >>> carro.acelerar()
    >>>carro.calculat_velocidade()
    2
    >>> carro.frear()
    >>>carro.calculat_velocidade()
    0

    >>> carro.calcular_direcao()
    >>> 'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    >>> 'Leste'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    >>> 'Sul'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    >>> 'Oeste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    >>> 'Sul'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    >>> 'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    >>> 'Norte'
"""
