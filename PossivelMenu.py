from corpos import Corpos, Planeta, Estrela, Lua, Asteroide

class Menu(Corpos):
    def __init__(self):
        self.opcoes = {
            "1": self.insere_corpos,
            "2": self.exibe_media,
            #"3": self.exibe_desvio,
            #"4": self.exibe_distancia,
            #"5": self.exibe_forca
            "6": self.exibe_lista
            #"7": self.exibe_movimento
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
        n = int(input("->Digite a quantidade de corpos há ser inserido: "))
        for i in range(0, n):
            categoria = input("\n->Categoria do corpo:\n1 para Planeta\n2 para Estrela\n3 para Lua\n4 para Asteroide"
            "\nEscolha uma opção: ")
            if (categoria == '1' or categoria == '2' or categoria == '3' or categoria == '4'):
                if categoria == "1":
                    corpo_celeste = Planeta('', 0.0, 0.0, 0.0, 0.0)
                    corpo_celeste.insere_cadastro()
                elif categoria == "2":
                    corpo_celeste = Estrela('', 0.0, 0.0, 0.0, 0.0)
                    corpo_celeste.insere_cadastro()
                elif categoria == "3":
                    corpo_celeste = Lua('', 0.0, 0.0, 0.0, 0.0)
                    corpo_celeste.insere_cadastro()
                elif categoria == "4":
                    corpo_celeste = Asteroide('', 0.0, 0.0, 0.0, 0.0)
                    corpo_celeste.insere_cadastro()
            else:
                print("\nAtenção!\nEscolha uma opção válida!")
    
    @staticmethod
    def exibe_media():
      if(len(Corpos.lista_corpos) != 0):
          print(f"\nA média das massas é {Corpos.calcula_media(Corpos.lista_corpos, 'massa')}")
      else:
          Menu.mostra_aviso()

    @staticmethod
    def exibe_lista():
        if (len(Corpos.lista_corpos) != 0):
            Corpos.ordena_lista(Corpos.lista_corpos, 'massa')
        else:
            Menu.mostra_aviso()
