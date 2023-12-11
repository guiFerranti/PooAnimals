class Dono:
    def __init__(self, nome_dono, idade_dono):
        self.nome_dono = nome_dono
        self.idade_dono = idade_dono
        self.animais = []

    def mostrar_informacoes(self):
        info_animais = "\n".join([animal.mostrar_informacoes() for animal in self.animais])
        return f"Nome do Dono: {self.nome_dono}\nIdade do Dono: {self.idade_dono}\nAnimais:\n{info_animais}"


class Animal:
    def __init__(self, nome, idade, genero, dono=None):
        self.nome = nome
        self.idade = idade
        self.genero = genero
        self.dono = dono
        if dono:
            dono.animais.append(self)

    def mostrar_informacoes(self):
        return f"Nome: {self.nome}\nIdade: {self.idade}\nGenero: {self.genero}"


class Mamifero(Animal):
    def __init__(self, nome, idade, genero, cor, dono=None):
        super().__init__(nome, idade, genero, dono)
        self.cor = cor

    def mostrar_informacoes(self):
        return super().mostrar_informacoes() + f"\nCor: {self.cor}"


class Reptil(Animal):
    def __init__(self, nome, idade, genero, escama, dono=None):
        super().__init__(nome, idade, genero, dono)
        self.escama = escama

    def mostrar_informacoes(self):
        return super().mostrar_informacoes() + f"\nEscama: {self.escama}"


class Ave(Animal):
    def __init__(self, nome, idade, genero, cor_pena, dono=None):
        super().__init__(nome, idade, genero, dono)
        self.cor_pena = cor_pena

    def mostrar_informacoes(self):
        return super().mostrar_informacoes() + f"\nCor da pena: {self.cor_pena}"


class Peixe(Animal):
    def __init__(self, nome, idade, genero, tipo_agua, dono=None):
        super().__init__(nome, idade, genero, dono)
        self.tipo_agua = tipo_agua

    def mostrar_informacoes(self):
        return super().mostrar_informacoes() + f"\nTipo de água: {self.tipo_agua}"


lista_donos = []

while True:
    opcao = input("1 - Cadastrar Mamífero"
                  "\n2 - Cadastrar Réptil"
                  "\n3 - Cadastrar Ave"
                  "\n4 - Cadastrar Peixe"
                  "\n5 - Listar Donos e Animais"
                  "\n6 - Sair"
                  "\nDigite a opção desejada: ")

    if opcao == '1':
        nome = input("Digite o nome do mamífero: ")
        idade = int(input("Digite a idade do mamífero: "))
        genero = input("Digite o genero do mamífero: ")
        cor = input("Digite a cor do mamífero: ")

        print("\nDonos disponíveis:")
        for idx, dono in enumerate(lista_donos, start=1):
            print(f"{idx} - {dono.nome_dono} ({dono.idade_dono} anos)")

        escolha_dono = input("\nEscolha um dono existente (digite o número) ou pressione Enter para criar um novo dono: ")
        
        if escolha_dono and escolha_dono.isdigit() and 1 <= int(escolha_dono) <= len(lista_donos):
            dono = lista_donos[int(escolha_dono) - 1]
        else:
            nome_dono = input("Digite o nome do dono: ")
            idade_dono = int(input("Digite a idade do dono: "))
            dono = Dono(nome_dono, idade_dono)
            lista_donos.append(dono)

        animal = Mamifero(nome, idade, genero, cor, dono)

    elif opcao == '2':
        nome = input("Digite o nome do réptil: ")
        idade = int(input("Digite a idade do réptil: "))
        genero = input("Digite o genero do réptil: ")
        escama = input("Digite a escama do réptil: ")

        print("\nDonos disponíveis:")
        for idx, dono in enumerate(lista_donos, start=1):
            print(f"{idx} - {dono.nome_dono} ({dono.idade_dono} anos)")

        escolha_dono = input("\nEscolha um dono existente (digite o número) ou pressione Enter para criar um novo dono: ")
        
        if escolha_dono and escolha_dono.isdigit() and 1 <= int(escolha_dono) <= len(lista_donos):
            dono = lista_donos[int(escolha_dono) - 1]
        else:
            nome_dono = input("Digite o nome do dono: ")
            idade_dono = int(input("Digite a idade do dono: "))
            dono = Dono(nome_dono, idade_dono)
            lista_donos.append(dono)

        animal = Reptil(nome, idade, genero, escama, dono)

    elif opcao == '3':
        nome = input("Digite o nome da ave: ")
        idade = int(input("Digite a idade da ave: "))
        genero = input("Digite o genero da ave: ")
        cor_pena = input("Digite a cor da pena da ave: ")

        print("\nDonos disponíveis:")
        for idx, dono in enumerate(lista_donos, start=1):
            print(f"{idx} - {dono.nome_dono} ({dono.idade_dono} anos)")

        escolha_dono = input("\nEscolha um dono existente (digite o número) ou pressione Enter para criar um novo dono: ")
        
        if escolha_dono and escolha_dono.isdigit() and 1 <= int(escolha_dono) <= len(lista_donos):
            dono = lista_donos[int(escolha_dono) - 1]
        else:
            nome_dono = input("Digite o nome do dono: ")
            idade_dono = int(input("Digite a idade do dono: "))
            dono = Dono(nome_dono, idade_dono)
            lista_donos.append(dono)

        animal = Ave(nome, idade, genero, cor_pena, dono)

    elif opcao == '4':
        nome = input("Digite o nome do peixe: ")
        idade = int(input("Digite a idade do peixe: "))
        genero = input("Digite o genero do peixe: ")
        tipo_agua = input("Digite o tipo de água do peixe: ")

        print("\nDonos disponíveis:")
        for idx, dono in enumerate(lista_donos, start=1):
            print(f"{idx} - {dono.nome_dono} ({dono.idade_dono} anos)")

        escolha_dono = input("\nEscolha um dono existente (digite o número) ou pressione Enter para criar um novo dono: ")
        
        if escolha_dono and escolha_dono.isdigit() and 1 <= int(escolha_dono) <= len(lista_donos):
            dono = lista_donos[int(escolha_dono) - 1]
        else:
            nome_dono = input("Digite o nome do dono: ")
            idade_dono = int(input("Digite a idade do dono: "))
            dono = Dono(nome_dono, idade_dono)
            lista_donos.append(dono)

        animal = Peixe(nome, idade, genero, tipo_agua, dono)

    elif opcao == '5':
        for dono in lista_donos:
            print(dono.mostrar_informacoes())
            print("==================================================================")

    elif opcao == '6':
        break
