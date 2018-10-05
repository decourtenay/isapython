a = {1: 2, 2: 4, 0:4}
print(a)
print(a.keys())
print(a.values())
print(a.items())

for key in a:
# to samo co for key in a.keys():
    print(key, a[key])

for key, val in a.items():
    print(key, val)