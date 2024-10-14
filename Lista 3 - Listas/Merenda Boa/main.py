dishes = [] # Lista de pratos
dishesAverage = 0 # Médias dos pratos

name = input() # Nome do avaliador
count = int(input()) # Qtd de Pratos

for i in range(0, count): # Loop de Qtd de Pratos
    dish = input() # Input de prato e nota
    newDish = dish.split("-") # Lista com prato e nota
    
    found = False
    for j in range(len(dishes)): # Checar se o prato ja existe na lista
        if newDish[0] == dishes[j][0]: # se esse prato ja existe
            if int(newDish[1]) == int(dishes[j][1]): # se a nota desse prato for igual a um da lista, recolocar na lista
                dishes.pop(j)
                dishes.append(newDish)
            elif int(newDish[1]) > int(dishes[j][1]): # se a nota do novo prato for maior a um da lista, substituir nota
                dishes[j][1] = newDish[1]
            found = True
            break
    if not found: # se prato não existir na lista, coloca-lo na lista
        dishes.append(newDish)

for i in range(len(dishes)): # adicionar as notas da lista
    dishesAverage += int(dishes[i][1])
dishesAverage /= len(dishes) # calcular média da lista

NewDishes = [dish[:] for dish in dishes] # copiar pratos antigos em novos pratos
RegradedDishes = [] # pratos que tiveram suas notas mudadas
NewDishesAverage = 0 # media das novas notas
count = int(input()) # Qtd de novos pratos

for i in range(0, count): # loop qtd de novos pratos
    dish = input() # novo prato e nota
    newDish = dish.split("-") # lista novo prato e nota
    
    found = False
    for j in range(len(NewDishes)): # loop para achar notas iguais
        if newDish[0] == NewDishes[j][0]: # se novo prato for igual a um novo prato da lista, mudar nota do novo prato
            found = True
            NewDishes[j][1] = newDish[1]
            RegradedDishes.append(newDish[:]) # adicionar a pratos reavaliados
            break
    if not found: # se novo prato não for igual a novos pratos da lista, adicionar a lista
        NewDishes.append(newDish)

for i in range(len(NewDishes)): # adicionar notas da lista de novos pratos
    NewDishesAverage += int(NewDishes[i][1])
NewDishesAverage /= len(NewDishes) # calcular media

print(f"AVALIAÇÃO DE {name.upper()}:")
grades = [str(i[1]).strip() for i in dishes] # lista das notas dos pratos
print(", ".join(grades))
print(f"Média inicial: {int(dishesAverage)}")

NewGrades = [str(i[1]).strip() for i in NewDishes] # lista das notas de novos pratos
print(", ".join(NewGrades))
print(f"Média final: {int(NewDishesAverage)}")

if len(NewDishes) > len(dishes): # checar se a qtd de novos pratos é maior que o dos pratos
    print("Os potenciais novos sarros experimentados foram:")
    PotentialDishes = [] # novos potencias pratos
    for i in range(len(dishes), len(NewDishes)): # se sim, adicionar esses novos potenciais pratos a lista
        PotentialDishes.append(NewDishes[i][0])
    print(", ".join(PotentialDishes)) 

OldRegradedDishes = [] # lista de pratos com notas reavaliadas

if len(RegradedDishes) > 0: # se tiver pratos reavaliados
    for i in range(len(dishes)): # se o novo prato reavaliado for igual a um prato na lista, adicionar a antigo pratos reavaliados
        for j in range(len(RegradedDishes)):
            if dishes[i][0] == RegradedDishes[j][0]:
                OldRegradedDishes.append(dishes[i])
    for i in range(len(RegradedDishes)): # para pratos reavaliados, fazer diferença das notas
        print(f"{RegradedDishes[i][0]}: {int(RegradedDishes[i][1]) - int(OldRegradedDishes[i][1])}")
elif len(RegradedDishes) == 0: # se não tiver novos pratos reavaliados, print
    print("Sem mudanças em receitas anteriores.")