# range includes 0 at index 0
a = list(range(100))
print(a[50::2])
print(a[50])

# pusta lista - niewykonalne zadanie (ale nie błąd)
print(a[50:60:-1])

b = list(range(1,100))
print(b[0])

# 41, indeksowanie zwraca nową listę zaczynającą się od 0
print(a[40:50][1:2])

e = print(a[40:50][0:5][0:1])

# przyporządkować do listy listę
a = [1, 2, 3]
b = ['inna_wartość']
a[2] = b
print(a)
b.append(5) # odwołanie do listy przez "b"
a[2].append(5)  # odwołanie do listy przez indeks listy "a"
print(a)
print(b)

# a[2] = 8
# print(a)

del b # kasowanie zmiennej
print(a)
print(b)