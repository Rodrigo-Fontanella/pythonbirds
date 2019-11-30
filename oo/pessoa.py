class Pessoa:

    # ele instancia atributos iniciais para a função, nome e idade
    def __init__(self, *filhos, nome=None, idade=44): # O * significa múltiplos objetos para filhos
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos) #cria um atributo de lista filhos


    #cria outro método
    def cumprimentar(self):
        return f'Olá! {id(self)}' #Cria uma f string

    #Quando inicia imprime o conteúdo para cada situação
if __name__ == '__main__':
    # Atribui um valor para a Classe
    rodrigo = Pessoa(nome='rodrigo')
    izauro = Pessoa(rodrigo, nome='Izauro') #Atribuo rodrigo ao izauro

    #Imprime o método cumprimentar "Padrão"
    print(Pessoa.cumprimentar(rodrigo)) #Pega o caminho da classe (Pessoa), depois vai na função (cumprimentar) e joga o "p"

    #Aqui ele imprime a ID da Classe Pessoa
    print(id(rodrigo))

    #Imprime o método cumprimentar de forma compacta
    print(rodrigo.cumprimentar())

    #Imprime o conteúdo do atributo nome da classe Pessoa, atribuído de Fontanella na parte de cima
    print(rodrigo.nome)

    print(Pessoa().nome) #Nesse aqui, pega o nome=None

    print(rodrigo.idade) #Imprime a idade, atributo da Classe Pessoa

    rodrigo.idade = 55 #Atribui uma nova idade a rodrigo
    print(rodrigo.idade)

    for filho in izauro.filhos: #para cada filho do objeto izauro.filhos
        print(filho.nome)





