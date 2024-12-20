def createPlayers(*args):
    validPosition = False
    validName = False
    player = input()
    playerInfo = player.split("-")
    
    if len(playerInfo) == 3: # se input for {jogador}-{posição}-{peso}, continua
        if playerInfo[1] == 'reserva': # se posição for reserva, continua
            if playersPosition.count('reserva') < 3: # se tiver 2 ou menos reservas no time, adiciona
                playersName.append(playerInfo[0])
                playersPosition.append(playerInfo[1])
                playersWeight.append(int(playerInfo[2]))  
            else: # se qtd de reservas maior ou igual a 3, mostra mensagem
                return print("Amigo, eu vou te falar só uma coisa... Olha essa formação aí!")
        else: # se input for qualquer posição menos reserva, continua
            if playerInfo[1] in POSITIONS and playerInfo[1] not in playersPosition: # se a posição do jogador for valido e não repetida, variavel booleana
                validPosition = True
            if playerInfo[0] not in playersName: # se nome for válido, variavel booleana
                validName = True
            if validPosition and validName: # se tudo estiver valido, adiciona ao time
                playersName.append(playerInfo[0])
                playersPosition.append(playerInfo[1])
                playersWeight.append(int(playerInfo[2]))
            else: # se algo não estiver valido, mostra mensagem
                return print("Amigo, eu vou te falar só uma coisa... Olha essa formação aí!")
    elif len(playerInfo) == 1: # se input for {jogador}, continua
        if playersPosition.count('reserva') < 3:
            playersName.append(playerInfo[0])
            playersPosition.append('reserva')
            playersWeight.append(3)
        else: # se 3 ou mais reservas, mostra mensagem
            return print("Amigo, eu vou te falar só uma coisa... Olha essa formação aí!")
    else: # qualquer outro caso estranho, mostra mensagem
        return print("Amigo, eu vou te falar só uma coisa... Olha essa formação aí!")
    
    if args: # se o jogador for adicionado no loop while true
        return print(f'Ele veste a camisa, é com garra, é com amor. {playerInfo[0]} representando como {playersPosition[-1]}.')

def teamCallout():
    if not playersName: # se a quantidade de jogadores for zero, para
        return print("Não é possível, Arnaldo!")        
    for i in range(len(playersName)): # se não for, mostra jogadores
        print(f"{playersName[i]}-{playersPosition[i]}")  
    
    return

def rating(*args):
    rate = sum(playersWeight) # soma dos pesos
    
    if args: # para somente a nota do time, retorna a nota
        return rate
    else: # caso não precise da nota, continua
        if rate < 25:
            print(f"A zaga tá batendo cabeça, o meio de campo tá perdido, sem criatividade. E o ataque? Isolado, sem receber uma bola decente! Assim não dá!. No máximo, o {team} é uns {rate} na escala!")
        elif rate > 25 and rate < 45:
            print(f"Esse time tem qualidade, tem talento, mas tá faltando encaixar o jogo! O {team}... é uns... {rate} ali na escala.")
        elif rate > 45:
            print(f"O elenco é fortíssimo: tem goleiro experiente, zaga sólida, meio-campo técnico, e um ataque rápido e criativo. O {team} TÁ MUITO ACIMA: {rate} PRA MAIS, PRA MAIS, NA ESCALA!")
        return

def match():
    win = False
    matchRating = rating(1)
    rivalTeam = input()
    factor = input()
    rivalName, rivaldiff = rivalTeam.split("-")
    
    if factor == "A verdade é que a situação tá complicada... A favor desse time, não tem nada!":
        pass
    else: # para qualquer mensagem menos a de cima, continua
        teamFactor = factor.split(",")
        matchRating += len(teamFactor)
        
    if "1" in rivalName: # se o rival for do 1° ano, adiciona a nota
        matchRating +=  2
    elif "3" in rivalName: # se o rival for do 2° ano, retira da nota
        matchRating -= 2
    # dificuldades do rival
    if rivaldiff == "fácil":
        if matchRating >= 25:
            win = True
    elif rivaldiff == "normal":
        if matchRating >= 35:
            win = True
    elif rivaldiff == "difícil":
        if matchRating >= 45:
            win = True
    
    if win: # caso vitória, mostra mensagem e retorna variavel booleana
        print(f'O apito final confirma a vitória! QUE ESPETÁCULO DO {team}. No fim, não teve como pro {rivalName}! Isso é futebol, meus amigos!')
        return win
    else: # caso derrota, mostra mensagem
        return print(f"Que tristeza, amigo! O time lutou, mas não conseguiu segurar o resultado. A torcida do {team}, que esteve em peso, agora vai embora cabisbaixa, dando espaço pro avanço do {rivalName}.")
        
NAMES = ["emerson.novaera", "erick.daselva", "valdelas", "marcella.linda123", "tamys.silva_br", "levi.ackerman", "mec.programadora", "alex_do_gerah"]
POSITIONS = ["goleiro", "pivô", "fixo", "ala esquerdo", "ala direito"]
playersName, playersPosition, playersWeight = [], [], []

name = input()

if name in NAMES: # se nome for válido na lista, continua
    pass
else: # se não for, para
    print("Desse jeito, vai complicar, meu amigo! Usuário da comissão não encontrado.")
    quit()

team = input()
teamQty = int(input())

if teamQty <= 8: # se qtd de jogadores for menor ou igual a 8, adiciona jogadores
    for i in range(teamQty):
        createPlayers()
elif teamQty == 0: # se qtd de jogadores for zero, mostra mensagem
    print("Não é possível, Arnaldo!")    
else: # para qualquer outro caso, continua
    pass

teamCallout()

while True:
    action = input()
    #casos para cada ação
    if action == "Quero agradecer de coração a você que nos acompanhou!":
        break
    elif action == "Olha só, amigo! Vamos pra mais da escalação do time:":
        createPlayers(1)
    elif action == "Olha o elenco ai, amigos da rede Porto!":
        teamCallout()
    elif action == "Arnaldo, e o que eu posso dizer desse time?":
        rating()
    elif action == "Vai rolar a bola! É emoção que não acaba mais, amigo! Haja coração! E aí, Arnaldo, me diz uma coisa: o que tem a favor desse time?":
        match()
    else:
        print("COMANDO NÃO RECONHECIDO.")