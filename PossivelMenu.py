from corpos import Corpos, Planeta, Estrela, Lua, Asteroide

class Menu(Corpos):
    def __init__(self):
        self.opcoes = {
            "1": self.insere_corpos,
            "2": self.exibe_media,
            "3": self.exibe_desvio_padrao,
            "4": self.exibe_distancia_media,
            #"5": self.exibe_forca_gravitacional
            "6": self.exibe_lista
            #"7": self.exibe_mudanca_coordenada
            #"8": self.sair
            }
            
    def mostra_menu(self):
        print("\n-----------------------------------------"
        "\n->1.Inserir um corpo\n"
        "->2.Calcular média da massa dos corpos\n"
        "->3.Calcular o desvio padrão das massas\n"
        "->4.Calcular a distância média dos corpos\n"
        "->5.Calcular força gravitacional entre os corpos\n"
        "->6.Listar corpos por massa\n"
        "->7 Mover corpos\n"
        "->8.Sair\n"
        "-----------------------------------------")

    def executa_programa(self):
        while True:
            self.mostra_menu()
            escolha = input("->Escolha uma opção: ")
            acao = self.opcoes.get(escolha)
            if acao:
                acao()
            else:
                print("\nAtenção!\nEscolha uma opção válida!")

    @staticmethod
    def mostra_aviso():
        print("\nAtenção!\n" "\nInsira ao menos um corpo!\n")
        
    @staticmethod
    def insere_corpos():
        categorias = {'1': Planeta('', 0.0, 0.0, 0.0, 0.0), '2': Estrela('', 0.0, 0.0, 0.0, 0.0), 
        '3': Lua('', 0.0, 0.0, 0.0, 0.0), '4': Asteroide('', 0.0, 0.0, 0.0, 0.0)}
        n = int(input("->Digite a quantidade de corpos há ser inserido: "))
        for i in range(0, n):
            categoria = input("\n->Categoria do corpo:\n1 para Planeta\n2 para Estrela\n3 para Lua\n4 para Asteroide"
            "\nEscolha uma opção: ")
            if (categoria == '1' or categoria == '2' or categoria == '3' or categoria == '4'):
                corpo_celeste = categorias[categoria]
                corpo_celeste.insere_cadastro()
            else:
                print("\nAtenção!\nEscolha uma opção válida!")
    
    #exibe calculos 

    @staticmethod
    def exibe_media():
      if(len(Corpos.lista_corpos) != 0):
          print(f"\nA média das massas é {Corpos.calcula_media(Corpos.lista_corpos, '_massa')}")
      else:
          Menu.mostra_aviso()

    @staticmethod
    def exibe_lista():
        if (len(Corpos.lista_corpos) != 0):
            Corpos.ordena_lista(Corpos.lista_corpos, '_massa')
        else:
            Menu.mostra_aviso()

    @staticmethod
    def exibe_desvio_padrao():
        if(len(Corpos.lista_corpos) != 0):
            media = Corpos.calcula_media(Corpos.lista_corpos, '_massa')
            print("\nO desvio padrão das massas é", Corpos.calcula_desvio(media, Corpos.lista_corpos, '_massa'))
        else:
            Menu.mostra_aviso()

    @staticmethod
    def exibe_distancia_media():
        distancia = []
        if(len(Corpos.lista_corpos) != 0):
            for idx, x in enumerate(Corpos.lista_corpos):
                for idy, y in enumerate(Corpos.lista_corpos[idx+1:], start=idx+1):
                    distancia.append(Corpos.calcula_distancia_media(x, y, '_x', '_y', '_z'))
                    print(f"\nA distância do corpo {x.nome} até o corpo {y.nome}" 
                    f" é de {distancia[-1]}")
            print(f'\nDistância média: {sum(distancia)/len(distancia)}')
        else:
            Menu.mostra_aviso()
