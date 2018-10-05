# Wyświetl do 10 pierwszych znaków pojawiających się w stringu (text).
# def print_10(text):
#     text_10 = text[0:10]
#     print(text_10)
#     for index, character in enumerate(text_10):
#         print(index + 1, character)

def print_10(text):
    used = []
    for char in text:
        if len(used) < 10:
            if char not in used:
                used.append(char)
    for char in used:
        count = text.count(char)
        print(char, count)


print_10('hpigigfyugpigiubiuipubigyvyuvuyvuyvyviuppviuviub/ff')

# # Wyśwetl do 10 pierwszych znaków pojawiających się w stringu
# # wraz z krotnościa ich wystąpienia.
# def print_10_count(text):
#     length = len(text)
#     counter = [0] * length
#     for character in text:
#         counter[character] = counter[character] + 1
#     print(character, counter[character])
#
# print_10_count('abrakadabr')

# Utrudnienie: Jako drugi parametr można podać listę znaków lub stringa
# - jeżeli została podana używamy do 10 znaków z niej,
# resztę uzupełniając pierwszymi znakami ze stringa
def print_10_hard(text, extra_list):
    pass
