# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.
# вычислите и выведите y

equation = 'y = -12x + 11111140.2121'
x = 2.5

a = equation.index("x")
ki = equation[4:int(a)]
bi = equation[int(a+4):]
k = float(ki)
b = float(bi)
y = k*x + b
print(equation)
print(x)
print(y)
