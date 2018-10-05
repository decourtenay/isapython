# Zażółć gęślą jaźń

vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'ę', 'ą']
polish = ['ą', 'ć', 'ę', 'ł', 'ń', 'ó', 'ś', 'ź', 'ż']
sentence = 'Zażółć gęślą jaźń'

print('Samogłoski')
for letter in sentence:
    if letter in vowels:
        print(letter)

print('\n')

print('Polskie znaki')
for letter in sentence:
    if letter in polish:
        print(letter)

print('\n')

print('Polskie znaki 2')
for letter in sentence:
    if ord(letter) > 127:
        print(letter)