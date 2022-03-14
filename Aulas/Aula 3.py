
from posixpath import split


a,b=1,2

if a > b:
    print('a é maior que b')
elif a < b:
    print('a é menor que b')
else:
    print ('a é igual a b')

l = [1,2, 3, 4, 5, 6,7, (1,2)]
d = {'key1': 'Herick', 'key2': 2, 'key3': 3.4}
t = (1, 2, 3, 4)

count_ = 0

for numb in l:
    print(numb)
    count_ += 1
print (count_)

for (keys, dict_) in d.items():
    print(keys, dict_)

lista = []
x = 1
while True:
    lista.append(x)
    x+=1
    if x>10:
        break

print(lista)