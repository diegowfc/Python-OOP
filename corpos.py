from classes import Planeta, Estrela, Lua, Asteroide

print("*******************")
print("Bem vindo!")
print("*******************")

lista_corpos = []

resposta = True
while resposta:
    print("\n-----------------------------------------"
          "\n->1.Inserir um corpo\n"
          "->2.Calcular média da massa dos corpos\n"
          "->3.Calcular o desvio padrão das massas\n"
          "->4.Calcular a distância média dos corpos\n"
          "->5.Calcular força gravitacional entre os corpos\n"
          "->6.Listar corpos por categoria\n"
          "->7 Mover corpos\n"
          "->8.Sair\n"
          "-----------------------------------------")
    resposta = input("->Escolha uma opção: ")
    if resposta == "1":
      n = int(input("->Digite a quantidade de corpos há ser inserido: "))
      for i in range(0, n):
        categoria = input("\n->Categoria do corpo:\n1 para Planeta\n2 para Estrela\n3 para Lua\n4 para Asteroide\nEscolha uma opção: ")
        nome = input(("\n->Insira o nome do corpo: "))
        massa = float(input("->Insira a massa do corpo: "))
        x = float(input("->Insira a coordenada x: "))
        y = float(input("->Insira a coordenada y: "))
        z = float(input("->Insira a coordenada z: "))
        if categoria == "1":
          lista_corpos.append(Planeta(nome, massa, x, y, z))
        elif categoria == "2":
          lista_corpos.append(Estrela(nome, massa, x, y, z))
        elif categoria == "3":
          lista_corpos.append(Lua(nome, massa, x, y, z))
        elif categoria == "4":
          lista_corpos.append(Asteroide(nome, massa, x, y, z))

    for corpo in lista_corpos:
      print(corpo.__dict__)
