from classes import Corpos, Planeta, Estrela, Lua, Asteroide

def mostra_aviso():
    print("\nAtenção!\n" "\nInsira ao menos um corpo!\n")


print("*******************\nBem vindo!\n*******************\n")

resposta = True
while resposta:
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
    resposta = input("->Escolha uma opção: ")
    if resposta == "1":
        n = int(input("->Digite a quantidade de corpos há ser inserido: "))
        for i in range(0, n):
            categoria = input("\n->Categoria do corpo:\n1 para Planeta\n2 para Estrela\n3 para Lua\n4 para Asteroide\nEscolha uma opção: ")
            if (categoria == '1' or categoria == '2' or categoria == '3' or categoria == '4'):
                nome = input(("\n->Insira o nome do corpo: "))
                massa = float(input("->Insira a massa do corpo: "))
                x = float(input("->Insira a coordenada x: "))
                y = float(input("->Insira a coordenada y: "))
                z = float(input("->Insira a coordenada z: "))
                print(f"\nCorpo com o nome {nome} inserido!\nPreencha as informações do novo corpo: ")
                if categoria == "1":
                    corpo_planeta = Planeta(nome, massa, x, y, z)
                    Corpos.adiciona_corpos(corpo_planeta)
                elif categoria == "2":
                    corpo_estrela = Estrela(nome, massa, x, y, z)
                    Corpos.adiciona_corpos(corpo_estrela)
                elif categoria == "3":
                    corpo_lua = Lua(nome, massa, x, y, z)
                    Corpos.adiciona_corpos(corpo_lua)
                elif categoria == "4":
                    corpo_asteroide = Asteroide(nome, massa, x, y, z)
                    Corpos.adiciona_corpos(corpo_asteroide)
            else:
                print("\nAtenção!\nEscolha uma opção válida!")
    elif resposta == "2":
        if (len(Corpos.lista_corpos) != 0):
            print(f"\nA média das massas é {Corpos.calcula_media(Corpos.lista_corpos, 'massa')}")
        else:
            mostra_aviso()
    elif resposta == "6":
        if (len(Corpos.lista_corpos) != 0):
            Corpos.ordena_lista(Corpos.lista_corpos, 'massa')
        else:
            mostra_aviso()
