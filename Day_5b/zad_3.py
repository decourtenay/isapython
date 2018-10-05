# Napisz funkcję podnoszącą podaną wartość (number) do podanej potęgi (index)
# Jeżeli potęga nie jest podana, podnieś do 2. potęgi


def my_pow(number, index=2):
    return number ** index


# my_pow(4, 3)   ## wynik: 64
# my_pow(2)    ## wynik: 4


print(my_pow(4, 3))
print(my_pow(2))
