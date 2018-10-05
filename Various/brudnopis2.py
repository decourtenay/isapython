# a = [4, 0, 3, 3, 9, 7, 0, 3, 3, 3]
# x = enumerate(a)
# print(list(x))
#
# # for x, number in enumerate(a):
# #     print(x, number)
# #
# # print(len(a))
#
# b = [0] * len(a) #Creates a counter
# for item in a:
#     b[item] = b[item] + 1
# for item in range(10):
#     print(item, b[item])
#
# for element in a:
#     element_squared = element**2
#     if element_squared != 0:
#         print(element_squared)
#     else:
#         print('Error')

names = ['Iwona', 'Zosia', 'Paweł', 'Miron']
years = [1981, 2009, 1977, 2012]

# names.append(input('Jak się nazywasz? '))
# years.append(input('W którym roku się urodziłeś? '))

for item in names:
    if item[-1] == 'a':
        born = 'urodziła się'
    else:
        born = 'urodził się'
    print(names.index(item), item, born, 'w', years[names.index(item)])

for index, item in enumerate(list(names)):
    print(index, item)

for index, item in enumerate(names, 1):
    print(index, item)

for item in enumerate(names):
    print(item)

a = enumerate(names)
print(a)