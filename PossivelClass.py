class Corpos:
    def __init__(self, nome, massa, x, y, z):
        self.nome = nome
        self.categoria = ""
        self.massa = massa
        self.x = x
        self.y = y
        self.z = z
    lista_corpos = []

    def cadastro(self, nome, massa, x, y, z):
        self.nome = input("\n->Insira o nome do corpo: ")
        self.massa = float(input("->Insira a massa do corpo: "))
        self.x = float(input("->Insira a coordenada x: "))
        self.y = float(input("->Insira a coordenada y: "))
        self.z = float(input("->Insira a coordenada z: "))

    def adiciona_corpos(self):
        Corpos.lista_corpos.append(self)
    
    def get_nome(self):
        return self.nome

    def get_categoria(self):
        return self.categoria

    def exibe_cadastro(self):
      return print(f"\nCorpo com o nome {self.get_nome()} e categoria {self.get_categoria()} inserido!"
                    "\n\nPreencha as informações do novo corpo: ")

    @staticmethod
    def mostra_aviso():
        print("\nAtenção!\n" "\nInsira ao menos um corpo!\n")

    @staticmethod
    def ordena_lista(lista, atributo):
        lista_ordenada = sorted(lista, key=lambda x: x.__dict__[atributo], reverse=True)
        for corpo in lista_ordenada:
            print(f"\n{corpo.__dict__}")
        return

    @staticmethod
    def calcula_media(lista, atributo):
        soma = 0
        for att in lista:
            soma += att.__dict__[atributo]
        resultado_media = soma / len(lista)
        return resultado_media

        
class Planeta(Corpos):
    def __init__(self, nome, massa, x, y, z):
        super().__init__(nome, massa, x, y, z)
        self.categoria = "planeta"

class Estrela(Corpos):
    def __init__(self, nome, massa, x, y, z):
        super().__init__(nome, massa, x, y, z)
        self.categoria = "estrela"

class Lua(Corpos):
    def __init__(self, nome, massa, x, y, z):
        super().__init__(nome, massa, x, y, z)
        self.categoria = "lua"

class Asteroide(Corpos):
    def __init__(self, nome, massa, x, y, z):
        super().__init__(nome, massa, x, y, z)
        self.categoria = "asteroide"
