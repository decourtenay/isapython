# Napisz funkcję wyświetlającą imię i nazwisko, nazwisko wielkimi literami



def name(first_name,last_name):
    print(first_name.capitalize() + ' ' + last_name.capitalize())  # Plusy nie są niezbędne w print()


name('pawel','nowak')
name(first_name = 'pawel', last_name = 'nowak')
a = 'pawel'
b = 'nowak'

name(a,b)

def print_square(x):
    print(x**2)

y = print_square(4)
print(y)

def give_square(x):
    return x**2

y = give_square(4)
print(y)