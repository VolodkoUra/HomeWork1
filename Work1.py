print("Hello World!")

number = 5
number_float = 5.5
name = "Yura"
boolean = True
print(number, number_float, name, boolean, end='\n')
print(number, number_float, name, boolean, sep='\n')
# print(' '.join([number,number_float,name,boolean]))

# Домашнее задание
a = -5
b = 7
print("Result: ", a + b)
print("Result: ", a - b)
print("Result: ", a * b)

# Вычислить выражение
result = (abs(a) + abs(b)) / (1 + abs(a * b))
print(result)

# Даны длинны ребра куба. Найти объём куба и площадь его боковой поверхности.
d = 2
v = d ** 3
print("Объем: ", v)
print("Площадь: ", d ** 2)

# Найти среднее арифмитическое и среднее геометрическое двух дайствительных чисел

n = 7
m = 8
result1 = (n + m) / 2
print(result1)
result2 = (n * m) ** (1 / 2)
print(result2)
