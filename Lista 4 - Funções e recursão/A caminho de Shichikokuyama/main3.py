def wordGuess():
    match = []
    matchWord = []
    index = 0

    while index < len(word):
        found = False
        for i, syllable in enumerate(SYLLABLES):
            if word[index:index+len(syllable)] == syllable:
                if syllable not in guessed:
                    guessed.append(syllable)
                    match.append(syllable)
                    matchWord.append((syllable, i))  # Track syllable and its index in SYLLABLES
                    
                index += len(syllable)
                found = True
                break
        if not found:
            index += 1

    # Check for consecutive syllables in SYLLABLES
    consecutive = True
    for j in range(len(matchWord) - 1):
        if matchWord[j][1] + 1 != matchWord[j + 1][1]:  # Check if indices are consecutive
            consecutive = False
            break
    
    # Print appropriate message
    if consecutive and len(matchWord) > 1:
        combined_word = ''.join([syllable for syllable, _ in matchWord])
        print(f"A palavra {combined_word} está toda no nome do hospital. Acertou em cheio, Totoro!")
    elif len(match) == 1:
        print(f"Lembrei! A sílaba {match[0]} está no nome do hospital. Obrigada, Totoro!")
    elif match:
        print(f"Lembrei! As sílabas: {', '.join(match)} estão no nome do hospital. Obrigada, Totoro!")
    else:
        print("Infelizmente nenhuma dessas sílabas me lembrou do nome do hospital, Totoro.")

# Example setup
SYLLABLES = ["shi", "chi", "ko", "ku", "ya", "ma"]
guessed = []

while True:
    if len(guessed) >= len(SYLLABLES):
        print("Conseguimos lembrar o nome do hospital shichikokuyama, agora é só pegar o Catbus e ir até lá!")
        break
        
    word = input()
    wordGuess()