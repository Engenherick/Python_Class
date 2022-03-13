"""
def somar(num1, num2):
    return (num1 + num2)
print(somar(5,7))
"""

def primos(numPrimo):
    count_ = 0
    for i in range(1, numPrimo):
        if numPrimo%i == 0: count_ += 1
        else: continue
    if count_ == 1: return print('É primo')
    else: return print ('Não é primo')

primos(29)