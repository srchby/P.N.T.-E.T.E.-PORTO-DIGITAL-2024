n = 0
i = 0

temp = 0
hung = 1
wifi = 0

while True:
    x = input()
    if x == "ir para o grad":
        temp -= 1
        wifi += 2
        continue
    if x == "sair para a rua":
        temp += 1
        continue
    if x == "comer uma quentinha":
        hung = 0
        continue
    if x == "conectar no wifi":
        wifi += 1
        continue

    if x == "parar":
        if temp >= 0:
            print("A temperatura aqui não está agradável")
        if temp <= -1:
            print("Agora sim, está aconchegante")
        if hung == 1:
            print("Meu corpo precisa de comida")
        if wifi <= 0:
            print("Essa conexão está horrível")
        if temp <= -1 and wifi >= 2 and hung == 0:
            print("Finalmente um lugar preciso para mim!")
        break
    
    else:
        print("Entrada inválida")
        continue