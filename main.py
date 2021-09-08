from corpos import Corpos

print("*******************")
print("Bem vindo!")
print("*******************")

massa = input('\nDigite a massa do corpo celeste: ');
corpo_celeste1 = Corpos(massa, 27)

print("Massa do corpo 1:", corpo_celeste1.massa)
