# number = 3
#
# number = number + 1
#
# print(number)
#
# print(number ** 2)
#
# print(number / 3)
#
# print(number // 3)
#
# print(number % 3)
#
# number = "3"
# print(number.isnumeric())
#
# print(0.1 + 0.1 + 0.1 != 0.3)

# a = 0
# int(a)
# print(a)
#
# print(float(a))

# counter = 10
# while counter:  #counter is true
#     print(counter)
#     counter = counter - 1
#     if counter < 5:
#         break

# range(10)
# print(range(10))
# print(list(range(10)))
# print(list(range(1, 10)))
# print(list(range(1, 10, 3)))
#
# a = 1
# while a < 10:
#     print(a)
#     a = a + 3
#
# a = 1
# while True:
#     if a >= 10:
#         break
#     print(a)
#     a = a + 3

#Lista
b = [1, 2, 3]
# print(type(b))
#
# c = '1'
# print(type(c))
#
# # MUTOWALNOŚć LISTY
# # metoda - funkcja przypisana do typu, pierwszy parametr ona sama
#
# b.append(5)
# print(b)
#
# b[1] = 'przypisanie'
# print(b)
#
# d = b.pop(1)
# print(b)
# print(d) #funkcja pop zwraca element z listy, zmienia listę

# c = [1]
#
# e = b + c
# print(e)
# print('e', e)
# print(*e)  # domyślny separator (spacja)
#
# e = []
# print(type(e))
#
# f = "Maciej"
# print(f[1:5:2])
# print(f[::2])
#
# # sortowanie
# h = [5, 3, 4]
# l = sorted(h)
# print(l)


n = [1, 3, 5]

for elem in n:
    print(elem+1)

for elem in range(1, 11):
    print(elem)

a = range(10)
for elem in a:
    print(elem)

p = 'Paweł'   # does not work, strings are immutable
p[0] = 'Gaweł'
p.append('d')



