# Przywitaj współpracowniczkę lub współpracownika
# sprawdź ostatnią literę imienia, żeby określić płeć

name = input("Podaj imię: ")

if name[-1] == "a" or name[-1] == "A":
    print("Witaj współpracowniczko")
else:
    print("Witaj współpracowniku")