def addPlayer(*args):
    positions = ["goleiro", "pivô", "ala esquerdo", "ala direito"]
    added = False
    sub = 0
    player = input()
    playerInfo = player.split("-")
    if len(playersName) + 1 <= 8: 
        if playerInfo[1] in positions:
            if playerInfo[1] == 'reserva' or len(playerInfo) == 1 and not playerInfo[0] in playersName:
                for i in range(len(playersPosition)):
                    if playersPosition[i] == 'reserva':
                        sub += 1
                if sub + 1 <= 3:
                    if playerInfo[1] == 'reserva':
                        playersName.append(playerInfo[0])
                        playersPosition.append(playerInfo[1])
                        playersWeight.append("3")
                        added = True
                    elif len(playerInfo) == 1:
                        playersName.append(playerInfo[0])
                        playersPosition.append("reserva")
                        playersWeight.append("3")
                        added = True
                else:
                    print("Amigo, eu vou te falar só uma coisa... Olha essa formação aí!")
            elif not playerInfo[1] in playersPosition and not playerInfo[0] in playersName:
                playersName.append(playerInfo[0])
                playersPosition.append(playerInfo[1])
                playersWeight.append(playerInfo[2])
                added = True
            else:
                print("Amigo, eu vou te falar só uma coisa... Olha essa formação aí!")
        else:
            print("Amigo, eu vou te falar só uma coisa... Olha essa formação aí!")
    else:
        print("Amigo, eu vou te falar só uma coisa... Olha essa formação aí!")
    
    if args and added:
        print(f"Ele veste a camisa, é com garra, é com amor. {playersName[-1]} representando como {playersPosition[-1]}.")
def teamCallout():
    for i in range(len(playersName)):
        print(f"{playersName[i]}-{playersPosition[i]}")   
def teamRating(*rivalFactor):
    teamRate = sum(int(weight) for weight in playersWeight)
    
    if rivalFactor:
        matchRating = rating
        matchRating += len(rivalFactor)          
        return matchRating
    else:
        return teamRate
def match():
    rivalTeam = input()
    rivalName, rivaldiff = rivalTeam.split("-")
    factor = input()
    if factor == "A verdade é que a situação tá complicada... A favor desse time, não tem nada!":
        pass
    elif not factor == "A verdade é que a situação tá complicada... A favor desse time, não tem nada!":
        rivalFactor = factor.split(",")
    matchRating = teamRating(rivalFactor)
    
    if rivalName[0] == "3":
        matchRating -= 2
    elif rivalName[0] == "1":
        matchRating += 2
        
    if rivaldiff == "fácil":
        if matchRating >= 25:
            win = True
        else: win = False
    elif rivaldiff == "normal":
        if matchRating >= 35:
            win = True
        else: win = False
    elif rivaldiff == "difícil":
        if matchRating >= 45:
            win = True
        else: win = False
    
    if win == True:
        print(f"O apito final confirma a vitória! QUE ESPETÁCULO DO {team}. No fim, não teve como pro {rivalName}! Isso é futebol, meus amigos!")
    elif win == False:
        print(f"Que tristeza, amigo! O time lutou, mas não conseguiu segurar o resultado. A torcida do {team}, que esteve em peso, agora vai embora cabisbaixa, dando espaço pro avanço do {rivalName}.")
    
    
names = ['emerson.novaera','erick.daselva','valdelas','marcella.linda123','tamys.silva_br','levi.ackerman','mec.programadora','alex_do_gerah']
name = input()
if name in names:
    pass
else:
    print("Desse jeito, vai complicar, meu amigo! Usuário da comissão não encontrado.")
    quit()

team = input()
playerTotal = int(input())

if playerTotal == 0:
    print("Não é possível, Arnaldo!")

playersName, playersPosition, playersWeight = [], [], []
for i in range(playerTotal):
    addPlayer()

teamCallout()

while True:
    rating = teamRating()  
    action = input()
    if action == "Quero agradecer de coração a você que nos acompanhou!":
        break
    elif action == "Olha só, amigo! Vamos pra mais da escalação do time:":
        addPlayer(1)
    elif action == "Olha o elenco ai, amigos da rede Porto!:":
        if playerTotal == 0:
            print("Não é possível, Arnaldo!")
        else:
            teamCallout()
    elif action == "Arnaldo, e o que eu posso dizer desse time?":
        if rating < 25:
            print(f"A zaga tá batendo cabeça, o meio de campo tá perdido, sem criatividade. E o ataque? Isolado, sem receber uma bola decente! Assim não dá!. No máximo, o {team} é uns {rating} na escala!")
        elif rating > 25 and rating < 45:
            print(f"Esse time tem qualidade, tem talento, mas tá faltando encaixar o jogo! O {team}... é uns... {rating} ali na escala.")
        elif rating > 45:
            print(f"O elenco é fortíssimo: tem goleiro experiente, zaga sólida, meio-campo técnico, e um ataque rápido e criativo. O {team} TÁ MUITO ACIMA: {rating} PRA MAIS, PRA MAIS, NA ESCALA!")
        teamCallout()
    elif action == "Vai rolar a bola! É emoção que não acaba mais, amigo! Haja coração! E aí, Arnaldo, me diz uma coisa: o que tem a favor desse time?":
        matchRating = rating
        match()
    else:
        print("COMANDO NÃO RECONHECIDO.")