def wordGuess():
    match = [] # para sílabas achadas
    matchWord = [] # para palavraas achadas
    index = 0
    
    while index < len(word):
        found = False
        for i, syllable in enumerate(SYLLABLES): # achar index e sílaba achada
            if word[index:index+len(syllable)] == syllable:
                if syllable not in guessed: # se sílaba não achada ainda
                    guessed.append(syllable)
                    match.append(syllable)
                    matchWord.append((syllable, i))
                    
                index += len(syllable)
                found = True
                break
        if not found: # se palavra/sílaba do input já achada
            index += 1
    
    isWord = True
    for j in range(len(matchWord) - 1): # se a palavra achada possui sílabas sequências
        if matchWord[j][1] + 1 != matchWord[j + 1][1]:
            isWord = False
            break
    
    guessedWord = "".join([syllable for syllable, _ in matchWord])
    if isWord and len(matchWord) > 1 and guessedWord == word: # se uma palavra foi achada e o input é igual a ela
        print(f"A palavra {''.join([syllable for syllable, _ in matchWord])} está toda no nome do hospital. Acertou em cheio, Totoro!")
    elif len(match) == 1: # se uma sílaba foi achada
        print(f"Lembrei! A sílaba {match[0]} está no nome do hospital. Obrigada, Totoro!")
    elif match: # se várias sílabas foram achadas
        print(f"Lembrei! As sílabas: {', '.join(match)} estão no nome do hospital. Obrigada, Totoro!")
    else: # se não foi achado
        print("Infelizmente nenhuma dessas sílabas me lembrou do nome do hospital, Totoro.")


SYLLABLES = ["shi","chi","ko","ku","ya","ma"]
guessed = []

while True:
    if len(guessed) >= len(SYLLABLES):
        print("Conseguimos lembrar o nome do hospital shichikokuyama, agora é só pegar o Catbus e ir até lá!")
        break
    
    word = input()  
    wordGuess()