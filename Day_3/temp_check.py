# Określ czy temperatura klimatyzacji jest prawidłowa
# z użyciem instrukcji warunkowych

temp = input("Jaka jest temperatura na klimatyzatorze? ")

if temp.isnumeric():
    temp = int(temp)
else:
    print("Wpisałeś błędną wartość")
    # Funkcja wychodzi z programu
    exit()

ideal_temp = 24.0

if temp < ideal_temp:
    print("Jest za zimno")
elif temp > ideal_temp:
    print("Jest za ciepło")
else:
    print("Temperatura jest idealna")

