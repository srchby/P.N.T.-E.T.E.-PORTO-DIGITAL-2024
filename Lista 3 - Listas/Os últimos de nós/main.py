bagsCount = int(input()) # qtd de mochilas

bagName = input() # nome das mochilas
bagNames = bagName.split(" ") # lista: nome das mochilas

bagSizes = [] # lista: tamanho das mochilas
for i in range(bagsCount): # for loop: para cada tamanho de mochila, adicionar a lista tamanho das mochilas
    bagSize = int(input())
    bagSizes.append(bagSize)

bagItems = [] # lista: items da mochila
for i in range(bagsCount): # for loop: para cada mochila, adicionar items Lanterna e Omega 3 da top therm
    bagItems.append(["Lanterna", "Omega 3 da top therm"])

itemCount = int(input()) # qtd de itens para as mochilas
for i in range(itemCount): # for loop: pela qtd de itens adicionados
    itemName = input() # nome do item
    itemIndex = int(input()) # mochila que será adicionado o item
    
    if len(bagItems[itemIndex]) + 1 <= bagSizes[itemIndex]: # if statement: se a lista de items da mochila mais o item for menor que o tamanho da mochila:
        bagItems[itemIndex].append(itemName)
    else: # else statement se a lista de items mais o item for maior que o tamanho da mochila
        print("Mochila cheia. Não vai dar para levar.")

while True: # while loop: enquanto não finalizar com "CHEGAMOS NO CIN!"
    action = input() # ação
    
    if action == "CHEGAMOS NO CIN!":
        for i in range(bagsCount): # for loop: para qtd de mochilas
            print(f"Mochila de {bagNames[i]} chegou assim:")
            for j in range(len(bagItems[i])): # for loop: para o número de items de cada mochila 
                print(f"{bagItems[i][j]}") # exibir cada item de cada mochila
        break

    elif action == "Tirar da mochila":
        removedItem = input() # nome do item que será removido
        removedIndex = int(input()) # mochila onde o item será removido

        found = False
        for i in range(len(bagItems[removedIndex])): # for loop: para conferir todos os items da mochila que terá um item removido:
            if bagItems[removedIndex][i] == removedItem: # if statement: se um item da mochila for igual ao item que será removido:
                bagItems[removedIndex].remove(removedItem)
                print(f"{removedItem} usado com sucesso da mochila {removedIndex}.")
                found = True
                break
        if not found: # if statement: se o item que será removido não for encontrado na mochila, exibir:
            print(f"Você não tem {removedItem} na mochila {removedIndex}.")
            
    elif action == "Guardar na mochila":
        addedItem = input() # item que será guardado na mochila
        addedIndex = int(input()) # mochila que terá um item guardado

        if len(bagItems[addedIndex]) + 1 <= bagSizes[addedIndex]: # if statement: se a qtd de items na mochila mais o novo item for menor que o tamanho da mochila:
            bagItems[addedIndex].append(addedItem) # adicionar novo item a mochila
            print(f"{addedItem} adicionado na mochila {addedIndex}.")
        else: # else statement: se a qtd de items mais o novo item for maior que o tamanho da mochila, exibir:
            print("Mochila cheia. Não vai dar para levar.")
    else: # else: statement: para qualquer outro caso, exibir:
        print("Ação inválida.")