def write_line(file_name, var_to_write):
    with open (file_name, 'a', encoding='utf-8') as file:
        file.write(var_to_write + '\n')

write_line('tekst3.txt', 'lalalalala')
write_line('tekst3.txt', 'papapapapa')
write_line('tekst3.txt', 'hahahahaha')


# skopiowanie pliku do nowego pliku
with open('tekst1.txt', 'r') as file:
    a = file.read()
    with open('tekst7.txt', 'w') as new_file:
        new_file.write(a)