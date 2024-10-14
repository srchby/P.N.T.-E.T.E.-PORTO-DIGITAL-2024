c = False
n = 0

while True:
    x = input()

    if x == "É o fim da Estrada pra Sheldon Cooper":
        if n == 0:
            print("Que potencial desperdiçado...")
        if n == 1 or n == 2:
            print("Tão perto, mas tão longe")
        if n == 3 or n == 4:
            print("Não desista Sheldon, você ainda têm muito para alcançar!")
        if n == 5:
            print("Nãoooooo, esse momento ia ser seu Sheldon")
        break
    elif x == "Ganhar o Nobel":
        if n == 5:
            print("Você conseguiu Sheldon, o Nobel é seu!!!")
        break

    elif x == "Bazinga" and c == True:
        n -= 1
        c = False

    elif x == "Começou a Trabalhar na Caltech":
        if n == 0:
            n += 1
            c = True
    elif x == "Trabalho sobre a String Theory":
        if n == 1:
            n += 1
            c = True
    elif x == "Ganhar o Chancellor de ciência":
        if n == 2:
            n += 1
            c = True
    elif x == "Pensar na Teoria de Cooper-Hofstader":
        if n == 3:
            n += 1
            c = True
    elif x == "Criou a Super Assimetria":
        if n == 4:
            n += 1
            c = True

    elif x == "Tinha que ser o engenheiro sem Phd do Wolowitz":
        print("Não xingue seus amigos Sheldon!")
        c = False
    elif x == "Leonard seu anão covarde":
        print("Não xingue seus amigos Sheldon!")
        c = False
    elif x == "Tu é muito burro Raj":
        print("Não xingue seus amigos Sheldon!")
        c = False
      
    else:
        c = False