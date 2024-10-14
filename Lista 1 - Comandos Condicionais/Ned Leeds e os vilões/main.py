xnam = input()
xpwr = int(input())
xlcl = int(input())
ynam = input()
ypwr = int(input())
ylcl = int(input())

xdstr = (xpwr ** 2 * xlcl) / 2
ydstr = (ypwr ** 2 * ylcl) / 2

if xpwr < 0 or ypwr < 0:
    print("Nem faco essa comparacao! Quero ser um vingador, busco coisas maiores.")
    exit()
    
if xpwr == ypwr:
    if xpwr % 2 == 0 or ypwr % 2 == 0:
        print("E quem disse que isso e problema meu? Vou chamar o senhor Stark.")
        exit()
    else:
        print("Vou chamar uns reforcos de outro universo... rsrs")
        exit()

if xdstr > ydstr:
    print(f"Com grandes poderes, vem grandes responsabilidades. Com isso, preciso ir deter o {xnam}.")
    exit()
if ydstr > xdstr:
    print(f"Com grandes poderes, vem grandes responsabilidades. Com isso, preciso ir deter o {ynam}.")
    exit()