x = input()
ope = input()
y = input()

try:
    x = int(x)
    y = int(y)
except ValueError:
    print("Luffy, você SUUUUPER não sabe usar isso, chama o Sanji!")
    exit()

if ope == "+":
    n = x + y
    print(f"O resultado é {n}")
elif ope == "-":
    n = x - y
    print(f"O resultado é {n}")
elif ope == "*":
    n = x - y
    print(f"O resultado é {n}")
elif ope == "/":
    n = x // y
    print(f"O resultado é {n}")
elif ope == "**":
    n = x ** y
    print(f"O resultado é {n}")
elif ope == "rad":
    n = x ** (1/y)
    print(f"O resultado é {n}")
else: 
    print("Luffy, você SUUUUPER não sabe usar isso, chama o Sanji!") 