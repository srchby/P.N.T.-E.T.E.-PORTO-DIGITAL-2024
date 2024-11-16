films = []
name = input()
count = int(input())

for i in range(0, count):
    film = input()
    newFilm = film.split(" - ")
    
    films.append(newFilm)

print(f"Os filmes sugeridos por {name} são:")

for i in range(len(films)):
    swapped = False
    for j in range(0, len(films) - i - 1):
      if films[j][1] < films[j + 1][1]:
        temp = films[j]
        films[j] = films[j+1]
        films[j+1] = temp
        swapped = True

    if not swapped:
      break
  
for i in range(0, count):
    print(f"{films[i][0]} - {films[i][1]}")