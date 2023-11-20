class Animal:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def mostrar_informacoes(self):
        print(f"Nome: {self.nome}\nIdade: {self.idade}\nTipo: {self.tipo}")


class Mamifero(Animal):
    def __init__(self, nome, idade, tipo, cor):
        super().__init__(nome, idade, tipo)
        self.cor = cor

    def mostrar_informacoes(self):
        super().mostrar_informacoes()
        print(f"Cor: {self.cor}")


class Reptil(Animal):
    def __init__(self, nome, idade, tipo, escama):
        super().__init__(nome, idade, tipo)
        self.escama = escama

    def mostrar_informacoes(self):
        super().mostrar_informacoes()
        print(f"Escama: {self.escama}")


class Ave(Animal):
    def __init__(self, nome, idade, tipo, cor_pena):
        super().__init__(nome, idade, tipo)
        self.cor_pena = cor_pena

    def mostrar_informacoes(self):
        super().mostrar_informacoes()
        print(f"Cor da pena: {self.cor_pena}")


class AnimalSilvestre(Animal):
    def __init__(self, nome, idade, tipo, ambiente):
        super().__init__(nome, idade, tipo)
        self.ambiente = ambiente

    def mostrar_informacoes(self):
        super().mostrar_informacoes()
        print(f"Ambiente: {self.ambiente}")


class Domestico(Animal):
    def __init__(self, nome, idade, tipo, nome_dono):
        super().__init__(nome, idade, tipo)
        self.nome_dono = nome_dono

    def mostrar_informacoes(self):
        super().mostrar_informacoes()
        print(f"Nome do dono: {self.nome_dono}")


animais = []

while True:
    opcao = input("1 - Cadastrar Mamífero\n2 - Cadastrar Réptil\n3 - Cadastrar Ave\n4 - Listar Animais\n5 - Sair\nDigite a opção desejada: ")

    if opcao == '1':
        nome = input("Digite o nome do mamífero: ")
        idade = int(input("Digite a idade do mamífero: "))
        tipo = input("Digite o tipo do mamífero: ")
        cor = input("Digite a cor do mamífero: ")
        animal = Mamifero(nome, idade, tipo, cor)
        animais.append(animal)

    elif opcao == '2':
        nome = input("Digite o nome do réptil: ")
        idade = int(input("Digite a idade do réptil: "))
        tipo = input("Digite o tipo do réptil: ")
        escama = input("Digite a escama do réptil: ")
        animal = Reptil(nome, idade, tipo, escama)
        animais.append(animal)

    elif opcao == '3':
        nome = input("Digite o nome da ave: ")
        idade = int(input("Digite a idade da ave: "))
        tipo = input("Digite o tipo da ave: ")
        cor_pena = input("Digite a cor da pena da ave: ")
        animal = Ave(nome, idade, tipo, cor_pena)
        animais.append(animal)

    elif opcao == '4':
        for animal in animais:
            animal.mostrar_informacoes()
            print("==================================================================")