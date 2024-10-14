n = 0
i = 0
joke = None
react = None

while joke != "Fim do Show!":
    joke = input()
    if joke == "Fim do Show!":
        break

    react = input()
    i += 1
    if react == "BAZINGA!":
        n += 1
        continue

if n > i * 0.6:
    print("BAZINGA! O senso de humor dele é muito bom, Amy, parece com o meu!")

if n <= i * 0.6 and n != 0:
    print("Esse stand up foi bastante mediano, Amy. Parece a carreira do Leonard!")

if n == 0:
    print("Amy, acredito que acabei de perder 60 de QI ouvindo essas piadas!")