# Oblicz wiek na podstawie roku urodzenia

birthyear = input("W którym roku się urodziłeś? ")
# Rzutowanie ze stringa na integer
birthyear = int(birthyear)
age = 2018 - birthyear
# Rzutowanie z integera na stringa
print("Twój wiek to " + str(age))