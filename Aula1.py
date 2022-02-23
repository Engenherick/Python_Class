from tkinter import commondialog

A, B = 1, 2.5
print ('Tipo do A:', type(A), '\nTipo do B:', type(B))
print ('Adição:', A+B)
print ('Subtração:', A-B)
print ('Multiplicação:', A*B)
print ('Divisão:', A/B)

############################## Utiizando referências
lucro, cidade, margem_de_lucro = 15000, 'Vaticano', 0.23
texto = ("A Cidade do %s com uma margem de lucro de %1.2f%% teve um lucro de R$%r" %(cidade, margem_de_lucro, lucro))
print(texto)

############################## Utilizando .format
texto = ("A Cidade do {cidade} com uma margem de lucro de {margem_de_lucro}% teve um lucro de R${lucro}").format(cidade = 'Vaticano', lucro = 15000, margem_de_lucro = 0.23)
print(texto)

############################## Após alterações realizadas