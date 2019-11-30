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
    rodrigo = Pessoa(nome='Rodrigo')
    lilian = Pessoa(nome='Lilian')
    bruno = Pessoa(nome='Bruno')

    izauro = Pessoa(rodrigo, lilian, bruno, nome='Izauro') #Atributo rodrigo ao izauro

    #Imprime o método cumprimentar "Padrão"
    print(Pessoa.cumprimentar(rodrigo)) #Pega o caminho da classe (Pessoa), depois vai na função (cumprimentar) e joga o id

    #Aqui ele imprime a ID da Classe Pessoa
    print(id(rodrigo))

    #Imprime o método cumprimentar de forma compacta
    print(rodrigo.cumprimentar())

    #Imprime o conteúdo do atributo nome da classe Pessoa, atribuído de Rodrigo na parte de cima
    print(rodrigo.nome)

    print(Pessoa().nome) #Nesse aqui, pega o nome=None

    print('Idade do Rodrigo:', rodrigo.idade) #Imprime a idade, atributo da Classe Pessoa

    izauro.idade = 70 #Atribui idade ao Izauro
    print('Idade do Izauro:', izauro.idade)

    for filho in izauro.filhos: #para cada filho do objeto izauro.filhos
        print('É filho do Sr. Izauro:', filho.nome)

    izauro.sobrenome = 'Brêtas' #Em qualquer lugar do código, posso criar atributos dinâmicos extras (não precisa ser dentro da Classe)
    print('Sobrenome Izauto:', izauro.sobrenome) #Lembrando que só serve para este atributo - não funciona para outro
    #Chama-se Adicionar Atributo em tempo de execução - - não é uma boa prática

    del rodrigo.filhos #deleta um atributo dinamicamente de rodrigo

    print(izauro.__dict__) #Puxa todos os atributos do Izauro - - -> Repare o sobrenome
    print(rodrigo.__dict__) #Puxa todos os atributos do Rodrigo

