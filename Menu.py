from corpos import Corpos, Planeta, Estrela, Lua, Asteroide

class Menu(Corpos):
    def __init__(self):
        self.opcoes = {
            "1": self.insere_corpos,
            "2": self.exibe_media,
            "3": self.exibe_desvio_padrao,
            "4": self.exibe_distancia_media,
            "5": self.exibe_forca_gravitacional,
            "6": self.exibe_lista,
            "7": self.exibe_mudanca_coordenada,
            "8": self.exibe_simulacao,
            "9": self.sair
        }
    resposta = True

    def mostra_menu(self):
        print("\n-----------------------------------------"
              "\n->1.Inserir um corpo\n"
              "->2.Calcular média da massa dos corpos\n"
              "->3.Calcular o desvio padrão das massas\n"
              "->4.Calcular a distância média dos corpos\n"
              "->5.Calcular força gravitacional resultante dos corpos\n"
              "->6.Listar corpos por massa\n"
              "->7.Mover corpos\n"
              "->8.Simular translações\n"
              "->9.Sair\n"
              "-----------------------------------------")

    def executa_programa(self):
        while self.resposta:
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


#EXIBE INFORMAÇÕES

    def insere_corpos(self):
        categorias = {
            '1': Planeta,
            '2': Estrela,
            '3': Lua,
            '4': Asteroide
        }
        n = int(input("->Digite a quantidade de corpos há ser inserido: "))
        for i in range(0, n):
            categoria = input("\n->Categoria do corpo:\n1 para Planeta\n2 para Estrela""\n3 para Lua\n4 para Asteroide"
                "\nEscolha uma opção: ")
            if (categoria == '1' or categoria == '2' or categoria == '3'or categoria == '4'):
                corpo_celeste = categorias[categoria]('', 0.0, 0.0, 0.0, 0.0)
                corpo_celeste.insere_cadastro()
            else:
                print("\nAtenção!\nEscolha uma opção válida!")

    def exibe_media(self):
        if (len(Corpos.lista_corpos) != 0):
            print(f"\nA média das massas é {Corpos.calcula_media('_massa')}")
        else:
            Menu.mostra_aviso()

    def exibe_desvio_padrao(self):
        if (len(Corpos.lista_corpos) != 0):
            media = Corpos.calcula_media('_massa')
            print("\nO desvio padrão das massas é",Corpos.calcula_desvio(media, '_massa'))
        else:
            Menu.mostra_aviso()

    def exibe_distancia_media(self):
        distancia = []
        if (len(Corpos.lista_corpos) != 0):
            for idx, x in enumerate(Corpos.lista_corpos):
                for idy, y in enumerate(Corpos.lista_corpos[idx + 1:], start=idx + 1):
                    distancia.append(Corpos.calcula_distancia_media(x, y, '_x', '_y', '_z'))
                    print(f"\nA distância do corpo {x.nome} até o corpo {y.nome}"
                        f" é de {distancia[-1]}")
            print(f'\nDistância média: {sum(distancia)/len(distancia)}')
        else:
            Menu.mostra_aviso()

    def exibe_forca_gravitacional(self):
        Corpos.lista_forca_resultante.clear()
        if (len(Corpos.lista_corpos) != 0):
            for idx, x in enumerate(Corpos.lista_corpos):
                Corpos.frx = 0
                Corpos.fry = 0
                Corpos.frz = 0
                for idy, y in enumerate(Corpos.lista_corpos[idx+1:], start=idx+1):
                    fr = Corpos.calcula_forca_resultante(x, y)
                Corpos.lista_forca_resultante.append(fr)
                print(f"\nA força resultante no corpo {x.nome} é de {Corpos.lista_forca_resultante[idx]}")
                Corpos.armazena_dados(x, idx, Corpos.lista_forca_resultante)             
        else:
            Menu.mostra_aviso()
            
    def exibe_lista(self):
        if (len(Corpos.lista_corpos) != 0):
            Corpos.ordena_lista('_massa')
        else:
            Menu.mostra_aviso()

    def exibe_mudanca_coordenada(self):
        if (len(Corpos.lista_corpos) != 0):
            Corpos.altera_coordenada('_nome')
        else:
            Menu.mostra_aviso()
    
    def exibe_simulacao(self):
        if (len(Corpos.lista_forca_resultante) != 0):
            Corpos.executa_simulacao()
        else:
            print(
            "\nAntes de realizar a simulação, é necessário calcular a força gravitacional resultante!"
            )

    def sair(self):
      print("\nPrograma finalizado!\nObrigado por usar!")
      self.resposta = False
