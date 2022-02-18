class Corpos:
    def __init__(self, nome, massa, x, y, z):
        self._nome = nome
        self._categoria = ""
        self._massa = massa
        self._x = x
        self._y = y
        self._z = z
    frx = 0
    fry = 0
    frz = 0
    lista_corpos = []
    lista_forca_resultante = []
    lista_simulacao = []

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

    @x.setter
    def x(self, novo_x):
        self._x = novo_x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, novo_y):
        self._y = novo_y

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, novo_z):
        self._z = novo_z

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

    def exibe_cadastro(self):
      return print(f"\nCorpo com o nome {self.nome} e categoria {self.categoria} inserido!"
      "\n\nEscolha uma opção: ")
    
    @staticmethod
    def ordena_lista(atributo):
        lista_ordenada = sorted(Corpos.lista_corpos, key=lambda x: x.__dict__[atributo], reverse=True)
        for corpo in lista_ordenada:
            print(f"\nNome: '{corpo.nome}', Categoria: '{corpo.categoria}', Massa: '{corpo.massa}',"
            f" X: '{corpo.x}', Y: '{corpo.y}', Z: '{corpo.z}'")
        return

    @staticmethod
    def altera_coordenada(atributo):
      corpo = input("\nDigite o nome do corpo que será movido: ")
      if(list(filter(lambda x: x.__dict__[atributo] == corpo, Corpos.lista_corpos))):
          for objeto in Corpos.lista_corpos:
              if(objeto.nome == corpo):
                  objeto.x = float(input(f"\n->Insira a nova coordenada x do corpo {corpo}: "))
                  objeto.y = float(input(f"\n->Insira a nova coordenada y do corpo {corpo}: "))
                  objeto.z = float(input(f"\n->Insira a nova coordenada z do corpo {corpo}: "))
      else:
          print("\nATENÇÃO!\nO nome digitado não foi cadastrado!\n\nNomes disponíveis:")
          for x in Corpos.lista_corpos:
              print(f"{x.nome}")
    
    @staticmethod
    def projeta_translacao():
        for corpo in Corpos.lista_corpos:
            escolha = int(input(f"\nPressione 1 se deseja mover o corpo {corpo.nome} ou 2 para manter a posição: "))
            if(escolha == 1):
                Corpos.altera_coordenada('_nome')
            elif(escolha == 2):
                continue
        return

    @staticmethod
    def armazena_dados(corpo, idx, lista):
        f = open("simulacao.txt", "a")
        f.write(
          f"Nome: '{corpo.nome}', Categoria: '{corpo.categoria}', Massa: '{corpo.massa}',"
          f" X: '{corpo.x}', Y: '{corpo.y}', Z: '{corpo.z}', "
          f" Força Resultante: '{lista[idx]}\n")
        return f.close()

    
#Calculos

    @staticmethod
    def calcula_media(atributo):
        soma = 0
        for corpo in Corpos.lista_corpos:
            soma += corpo.__dict__[atributo]
        resultado_media = soma / len(Corpos.lista_corpos)
        return resultado_media

    @staticmethod
    def calcula_desvio(media, atributo):
        desvio = 0
        for corpo in Corpos.lista_corpos:
            desvio += (((corpo.__dict__[atributo] - media)**2))
        desvio = (desvio / 3)**0.5
        return desvio

    @staticmethod
    def calcula_distancia_media(x, y, atributo1, atributo2, atributo3):
        dm = ((y.__dict__[atributo1] - x.__dict__[atributo1])**2 + (y.__dict__[atributo2] - x.__dict__[atributo2])**2 + (y.__dict__[atributo3] - x.__dict__[atributo3])**2)**0.5
        return dm 
    
    @staticmethod
    def calcula_forca_gravitacional(x, y, atributo):
        g = 6.67 * pow(10,-11)
        distancia = Corpos.calcula_distancia_media(x, y, '_x', '_y', '_z')
        forca_gravitacional = (g * ((x.__dict__[atributo] * y.__dict__[atributo])) / (pow(distancia,2)))
        return forca_gravitacional
            
    @staticmethod
    def calcula_forca_resultante(x, y):
        distancia = Corpos.calcula_distancia_media(x, y, '_x', '_y', '_z')
        delta_x = x.__dict__['_x'] - y.__dict__['_x'] 
        delta_y = x.__dict__['_y'] - y.__dict__['_y']
        delta_z = x.__dict__['_z'] - y.__dict__['_z']
        fx = (Corpos.calcula_forca_gravitacional(x, y, '_massa')*delta_x)/distancia
        try:
            fy = (fx* delta_y)/delta_x
            fz = (fy * delta_z)/delta_y
            Corpos.frx += fx
            Corpos.fry += fy
            Corpos.frz += fz
            forca_resultante = Corpos.frx ** 2 + Corpos.fry ** 2 + Corpos.frz ** 2
        except:
            forca_resultante = Corpos.frx ** 2 + Corpos.fry ** 2 + Corpos.frz ** 2
        return forca_resultante ** 0.5

    @staticmethod
    def executa_simulacao():
        Corpos.lista_forca_resultante.clear()
        Corpos.projeta_translacao()
        tempo = int(input("\nIndique o tempo da translação em anos: "))
        granularidade = int(input("\nDigite o tempo da granularidade da simulação: "))
        simulacao = tempo/granularidade
        f = open("simulacao.txt", "a")
        f.write("\nForca resultante após passo de simulação:")
        f.close()
        for idx, x in enumerate(Corpos.lista_corpos):
            Corpos.frx = 0
            Corpos.fry = 0
            Corpos.frz = 0
            for idy, y in enumerate(Corpos.lista_corpos[idx+1:], start=idx+1):
                fr = Corpos.calcula_forca_resultante(x, y)
            contador = 1
            while contador <= simulacao:
                forca_simulacao = fr / (contador/simulacao)
                f = open("simulacao.txt", "a")
                f.write(f"\nForca resultante em {x.nome} após o passo {contador} de simulação: {forca_simulacao}\n")
                f.close()
                contador += 1
            Corpos.lista_forca_resultante.append(fr)
        return print("\nDados armazenados no arquivo!")


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
