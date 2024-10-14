name = input() # Nomes para a lista
names = name.split(",") # Lista dos nomes

while True:
    if len(names) == 1:
        print(f"Acho que encontramos o suspeito. O seu nome é {names[0]}, vamos salvar o Sam!")
        break
        
    prompt = input() # Input para operações da lista
    
    if prompt == "Não encontrei nada no primeiro suspeito":
        names.pop(0)
    elif prompt == "O último da lista está limpo":
        names.pop(-1)
    elif prompt == "Procurei por um elemento um pouco mais além na lista e ele está acima de qualquer suspeita":
        names.pop(len(names) // 2)
    elif prompt == "Pelas minhas verificações, não encontrei nada de alarmante no indivíduo que está na seguinte posição:":
        index = int(input()) # Index do nome retirado da lista
        names.pop(index)
    elif prompt == "Acho que temos mais uma opção a ser analisada…":
        suspect = input() # Nome adicionado a lista 
        names.append(suspect)
    
    else:
        print("Isso não estava no combinado, a lista vai permanecer do mesmo jeito")