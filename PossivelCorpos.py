class Corpos:
    def __init__(self, nome, massa, x, y, z):
        self._nome = nome
        self._categoria = ""
        self._massa = massa
        self._x = x
        self._y = y
        self._z = z
    lista_corpos = []

    def cadastro(self, nome, massa, x, y, z):
        self._nome = input("\n->Insira o nome do corpo: ")
        self._massa = float(input("->Insira a massa do corpo: "))
        self._x = float(input("->Insira a coordenada x: "))
        self._y = float(input("->Insira a coordenada y: "))
        self._z = float(input("->Insira a coordenada z: "))
    
    def insere_cadastro(self):
      self.cadastro('nome','massa','x','y','z')
      Corpos.lista_corpos.append(self)
      self.exibe_cadastro()
    
    @property
    def nome(self):
        return self._nome

    @property
    def categoria(self):
        return self._categoria

    @property
    def massa(self):
        return self._massa
    
    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def z(self):
        return self._z

    def exibe_cadastro(self):
      return print(f"\nCorpo com o nome {self.nome} e categoria {self.categoria} inserido!"
      "\n\nPreencha as informações do novo corpo: ")

    @staticmethod
    def ordena_lista(lista, atributo):
        lista_ordenada = sorted(lista, key=lambda x: x.__dict__[atributo], reverse=True)
        for corpo in lista_ordenada:
            print(f"\nNome: '{corpo.nome}', Categoria: '{corpo.categoria}', Massa: '{corpo.massa}',"
            f" X: '{corpo.x}', Y: '{corpo.y}', Z: '{corpo.z}'")
        return

    @staticmethod
    def calcula_media(lista, atributo):
        soma = 0
        for corpo in lista:
            soma += corpo.__dict__[atributo]
        resultado_media = soma / len(lista)
        return resultado_media

    @staticmethod
    def calcula_desvio(media, lista, atributo):
        desvio = 0
        for corpo in lista:
            desvio += (((corpo.__dict__[atributo] - media)**2))
        desvio = (desvio / 3)**0.5
        return desvio


class Planeta(Corpos):
    def __init__(self, nome, massa, x, y, z):
        super().__init__(nome, massa, x, y, z)
        self._categoria = "planeta"

class Estrela(Corpos):
    def __init__(self, nome, massa, x, y, z):
        super().__init__(nome, massa, x, y, z)
        self._categoria = "estrela"

class Lua(Corpos):
    def __init__(self, nome, massa, x, y, z):
        super().__init__(nome, massa, x, y, z)
        self._categoria = "lua"

class Asteroide(Corpos):
    def __init__(self, nome, massa, x, y, z):
        super().__init__(nome, massa, x, y, z)
        self._categoria = "asteroide"
