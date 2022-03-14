lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = [7, 8, 9]

matrix = [lista1, lista2, lista3]

newlist1 = [row[0] for row in matrix]

print(newlist1)

##################################
print("******Dicionarios:******")
d = {'k1': [1,2,3]}
print(d['k1'][1])

#################################

t = (1, 2, 3, 4)
print(t)

#################################

my_file = open('text.txt')
print(my_file.read())
my_file.seek(0)
print(my_file.readline())