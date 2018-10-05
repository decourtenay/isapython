# Sprawdź czy liczba jest podzielna przez 3, 5 LUB 7

number = input("Podaj liczbę: ")

number = int(number)

# Znak modulo (%) oznacza resztę z dzielenia
if number % 3 == 0:
    print("Liczba jest podzielna przez 3")

if number % 5 == 0:
    print("Liczba jest podzielna przez 5")

if number % 7 == 0:
    print("Liczba jest podzielna przez 7")
