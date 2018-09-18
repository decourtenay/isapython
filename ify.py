# NAME
# name = input("Podaj imię: ")
#
# if name == "Jarema" or name == "Kosma":
#     print("Witaj kolego!")
# elif name[-1] == "a" or name[-1] == "A":
#     print("Cześć koleżanko!")
# else:
#     print("Witaj kolego!")

# TEMPERATURE
# temp = input("Jaka jest temperatura na klimatyzatorze? ")
#
# if temp.isnumeric():
#     temp = int(temp)
# else:
#     print("Wpisałeś błędną wartość")
#     exit()
#
# ideal_temp = 24.0
#
# if temp < ideal_temp:
#     print("Jest za zimno")
# elif temp > ideal_temp:
#     print("Jest za ciepło")
# else:
#     print("Temperatura jest idealna")

# PODZIELNOŚĆ
number = input("Podaj liczbę ")

if number.isnumeric():
    number = int(number)
else:
    print("Wpisałeś błędną wartość")
    exit()

if number % 3 == 0:
    print("Liczba jest podzielna przez 3")
else:
    print("Liczba nie jest podzielna przez 3")

if number % 5 == 0:
    print("Liczba jest podzielna przez 5")
else:
    print("Liczba nie jest podzielna przez 5")

if number % 7 == 0:
    print("Liczba jest podzielna przez 7")
else:
    print("Liczba nie jest podzielna przez 7")


