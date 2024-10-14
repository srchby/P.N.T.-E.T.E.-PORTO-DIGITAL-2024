"""
    Cidade 1
    Nota 1
    Distância 1
    Cidade 2
    Nota 2
    Distância 2
    Cidade 3
    Nota 3
    Distância 3
"""

x = input()
xgrad = float(input())
xdist = int(input())
y = input()
ygrad = float(input())
ydist = int(input())
z = input()
zgrad = float(input())
zdist = int(input())

if xgrad < 4 and ygrad < 4 and zgrad < 4:
    print("Nota mínima não atingida")
else:   
    if xgrad == ygrad == zgrad:
        if xdist < ydist and xdist < zdist:
            print(x)
        elif ydist < xdist and ydist < zdist:
            print(y)
        elif zdist < ydist and zdist < xdist:
            print(z)
            
    if xgrad > ygrad and xgrad > zgrad:
        print(x)
    elif ygrad > xgrad and ygrad > zgrad:
        print(y)
    elif zgrad > ygrad and zgrad > xgrad:
        print(z)
            
