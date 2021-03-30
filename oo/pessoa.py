class Pessoa:
    def __init__(self, *filhos, nome = None, idade=50):
        self.idade = idade
        self.nome = nome
        self.filhos =list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    claudio = Pessoa(nome='Claudio')
    rodrigo = Pessoa(claudio, nome='Rodrigo')
    print(Pessoa.cumprimentar(rodrigo))
    print(id(rodrigo))
    print(rodrigo.cumprimentar())
    print(rodrigo.nome)
    print(rodrigo.idade)
    for filho in rodrigo.filhos:
        print(filho.nome)
    rodrigo.sobrenome = 'Santos'
    rodrigo.esposa = 'Raquel'
    del rodrigo.esposa
    print(claudio.__dict__)
    print(rodrigo.__dict__)
