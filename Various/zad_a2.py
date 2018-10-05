# Licznik
# Pusta lista jest licznikiem
# Przy każdym wystąpieniu liczby w pierwszej liście, zwiększasz wartość na pozycji licznika o indeksie równym wartości z listy 1


a = [1,2,0,3,4,5,6,7,7,7,7,1,2,3]
b = [0] * 10
print(b)

for ii in a:
    b[ii] += 1 # b[ii] = b[ii] + 1
print(b)


a = [1,2,0,3,4,5,6,7,7,7,7,1,2,3]
b = [''] * 10
print(b)

for ii in a:
    b[ii] = b[ii] + 'x'
print(b)

# did but wrong reference i.e. a
d = ['x'*ii for ii in a]
print(d)