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
                    match.append(syllable)  # Track all found syllables
                    matchWord.append((syllable, i))  # Track both the syllable and its index in SYLLABLES
                    
                index += len(syllable)
                found = True
                break
        if not found:
            index += 1

    # Check if we have consecutive syllables in SYLLABLES
    if len(matchWord) > 1:
        indices = [index for _, index in matchWord]
        if all(indices[i] + 1 == indices[i + 1] for i in range(len(indices) - 1)):
            # Consecutive syllables are found in SYLLABLES
            print(f"A palavra {''.join([syllable for syllable, _ in matchWord])} está toda no nome do hospital. Acertou em cheio, Totoro!")
            return
    
    # Print the appropriate message based on the number of syllables found
    if len(match) == 1:  # Only one syllable found
        print(f"Lembrei! A sílaba {match[0]} está no nome do hospital. Obrigada, Totoro!")
    elif match:  # Multiple syllables found but not consecutive
        print(f"Lembrei! As sílabas: {', '.join(match)} estão no nome do hospital. Obrigada, Totoro!")
    else:
        print("Infelizmente nenhuma dessas sílabas me lembrou do nome do hospital, Totoro.")

# Example setup
SYLLABLES = ["shi", "chi", "ko", "ku", "ya", "ma"]
guessed = []

while True:
    word = input("Enter a word: ")
    wordGuess()
