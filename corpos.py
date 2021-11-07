class Corpos:
    def __init__(self, nome, massa, x, y, z ):
      self.nome = nome
      self.categoria = ""
      self.massa = massa
      self.x = x
      self.y = y
      self.z = z

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
