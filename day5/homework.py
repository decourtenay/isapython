# Napisz funkcję (z docstringiem) calc, która będzie wykonywała podstawowe
# działania arytmetyczne (dodawanie, odejmowanie, mnożenie, dzielenie).
# Funkcja powinna przyjmować 3 argumetny:
# działanie (jako string), argument 1, argument 2 (domyślnie o wartości 1).
# Wywołaj funkcję na podanej liście parametrów

print('\nWersja podstawowa\n')
def calc(operator, arg1, arg2 = 1):
    """Wykonywanie działań matematycznych na podanych parametrach"""
    if operator == '+':
        result = arg1 + arg2
    elif operator == '-':
        result = arg1 - arg2
    elif operator == '*':
        result = arg1 * arg2
    elif operator == '/':
        result = arg1 / arg2
    else:
        print('Przepraszam, takiego działania nie umiem wykonywać')
        exit()
    print('Wynik to', result)

test_parameters = [
    ('+', 2, 2),
    ('-', 5, 7),
    ('*', 6, 2.5),
    ('/', 4),
]

for tup in test_parameters:
    operator = tup[0]
    arg1 = tup[1]
    if len(tup) == 2:
        arg2 = 1
    else:
        arg2 = tup[2]
    calc(operator, arg1, arg2)

# Utrudnienie 1: Poproś o podanie parametrów przez konsolę

print('\nUtrudnienie pierwsze\n')

operator = input('Jakie działanie chcesz wykonać? ')
arg1 = float(input('Podaj pierwszą liczbę '))
arg2 = input('Podaj drugą liczbę ')
if arg2 != '':
    arg2 = float(arg2)
else:
    arg2 = 1
calc(operator, arg1, arg2)

# Utrudnienie 2: Wykorzystaj podaną funkcję w programie kalkulator,
# która najpierw zapyta o działanie (arytmetyczne lub przerwanie programu),
# a póżniej o argumenty działania

print('\nUtrudnienie drugie\n')

def calculator():
    """Pobranie od użytkownika parametrów, a następnie uruchomienie funkcji calc z tymi paramatrami"""
    print('Jakie działanie chcesz wykonać? ')
    operator = input('Dodawanie (+) Odejmowanie (-) Mnożenie (*) czy Dzielenie (/) ')
    if operator != '+' and operator != '-' and operator != '*' and operator != '/':
        # if operator not in ['+','-','*','/']:
        print('Przepraszam, takiego działania nie umiem wykonywać ')
        exit()
    arg1 = float(input('Podaj pierwszą liczbę '))
    if operator == '+':
        arg2 = input('Podaj liczbę, jaką chcesz do niej dodać ')
    elif operator == '-':
        arg2 = input('Podaj liczbę, jaką chcesz od niej odjąć ')
    elif operator == '*':
        arg2 = input('Podaj liczbę, przez jaką chcesz ją pomnożyć ')
    else:
        arg2 = input('Podaj liczbę, przez jaką chcesz ją podzielić ')
    if arg2 != '':
        arg2 = float(arg2)
    else:
        arg2 = 1
    calc(operator, arg1, arg2)

calculator()