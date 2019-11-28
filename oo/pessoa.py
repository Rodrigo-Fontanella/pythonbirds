class Pessoa:

    # ele instancia atributos iniciais para a função, nome e idade
    def __init__(self, nome=None, idade=44):
        self.idade = idade
        self.nome = nome

    #cria outro método
    def cumprimentar(self):
        return f'Olá! {id(self)}'

    #Quando inicia imprime o conteúdo para cada situação
if __name__ == '__main__':
    # Atribui um valor para a Classe
    p = Pessoa('Fontanella')

    #Imprime o método cumprimentar "Padrão"
    print(Pessoa.cumprimentar(p))

    #imprime a ID da Classe Pessoa
    print(id(p))

    #Imprime o método cumprimentar de forma compacta
    print(p.cumprimentar())

    #Imprime o conteúdo do atributo nome da classe Pessoa, atribuído de Fontanella
    print(p.nome)

    print(Pessoa().nome) #Nesse aqui, pega o nome=None

    p.nome = 'Rodrigo' #Atribui um novo nome ao p
    print(p.nome) #imprime o novo nome

    print(p.idade) #Imprime a idade, atributo da Classe Pessoa

    p.idade = 55 #Atribui outra idade
    print(p.idade)






