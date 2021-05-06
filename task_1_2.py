'''
Даны действительные числа x и y. Получить (|x|−|y|)/(1+|x*y|)
'''
x = 5
y = -7
result = (abs(x) + abs(y)) / (1 + abs(x * y))
print(result)