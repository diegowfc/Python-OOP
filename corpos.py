class Corpos:
    def __init__(self, nome, massa, x, y, z):
        self.nome = nome
        self.categoria = ""
        self.massa = massa
        self.x = x
        self.y = y
        self.z = z
    lista_corpos = []
    
    @staticmethod
    def adiciona_corpos(objeto):
        Corpos.lista_corpos.append(objeto)

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
