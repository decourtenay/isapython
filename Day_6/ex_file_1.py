sciezka = "tekst1.txt"

# otwieramy plik w trybie tekstowym, tylko do odczytu
plik = open(sciezka, 'r')

# read() czyta zawartość, od miejsca w któym jest kursor
# aż do kocńa pliku
tresc = plik.read()
print(tresc)

# pamiętać o zamykaniu pliku
plik.close()

with open("tekst1.txt", 'r') as tekst1:
    count = 1
    for line in tekst1:
        if count <= 3:
            print(line)
            count = count + 1
