def parenthesisCheck():
    openBracket = 0
    closeBracket = 0
    
    for char in sentence:
        if char == "(":
            openBracket += 1
        elif char == ")":
            closeBracket += 1
    
    if openBracket > closeBracket:
        print("A quantidade de parênteses '(' está maior que a de ')', vamos descartá-la")
    elif closeBracket > openBracket:
        print("A quantidade de parênteses ')' está maior que a de '(', vamos descartá-la")
    else:
        print("Essa sentença está com os parênteses balanceados, HOORAY!")

count = int(input())

for i in range(count):
    sentence = input()
    
    parenthesisCheck()