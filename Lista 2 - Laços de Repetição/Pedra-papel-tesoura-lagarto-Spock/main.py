n = int(input())

l = 'lagarto'
s = 'spock'
t = 'tesoura'

shw = 0
rajw = 0

for i in range(0, n):
    sh = input()
    raj = input()
    if sh == l and raj == s:
        shw += 1
    elif sh == s and raj == t:
        shw += 1
    elif sh == t and raj == l:
        shw += 1
    
    if raj == l and sh == s:
        rajw += 1
    elif raj == s and sh == t:
        rajw += 1
    elif raj == t and sh == l:
        rajw += 1


if shw > rajw:
    print("BAZINGA! EU SOU O SENHOR DA SALA!")
elif rajw > shw:
    print("ENGOLE ESSA, SHELDON!")
elif rajw == shw:
    print("Oh não, precisamos de outra rodada.")