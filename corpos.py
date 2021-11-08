class Corpos:
    def __init__(self, nome, massa, x, y, z ):
      self.nome = nome
      self.categoria = ""
      self.massa = massa
      self.x = x
      self.y = y
      self.z = z
    lista_corpos = []

    def adiciona_corpos(self):
      Corpos.lista_corpos.append(self)

    @staticmethod
    def ordena_lista(atributo):
      lista_ordenada = sorted(Corpos.lista_corpos, key=lambda x: x.massa, reverse=True)
      for corpo in lista_ordenada:
        print (f"\n{corpo.__dict__}")
    
    @staticmethod
    def mostra_aviso():
      print("\nAtenção!\n" "\nInsira ao menos um corpo!\n")

class Planeta(Corpos):
  def __init__(self, nome, massa, x, y, z ):
    super().__init__(nome, massa, x, y, z)
    self.categoria = "planeta"

class Estrela(Corpos):
  def __init__(self, nome, massa, x, y, z ):
    super().__init__(nome, massa, x, y, z)
    self.categoria = "estrela"

class Lua(Corpos):
  def __init__(self, nome, massa, x, y, z ):
    super().__init__(nome, massa, x, y, z)
    self.categoria = "lua"

class Asteroide(Corpos):
  def __init__(self, nome, massa, x, y, z ):
    super().__init__(nome, massa, x, y, z)
    self.categoria = "asteroide"
