import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt

# Метод прямоугольников
def rectangle_method(func, a, b, n):
    h = (b - a) / n
    integral = 0
    for i in range(n):
        x_i = a + i * h
        integral += func(x_i)
    integral *= h
    return integral

# Метод трапеций
def trapezoidal_method(func, a, b, n):
    h = (b - a) / n
    integral = (func(a) + func(b)) / 2
    for i in range(1, n):
        x_i = a + i * h
        integral += func(x_i)
    integral *= h
    return integral

# Метод Симпсона для вычисления интеграла
def simpson_method(func, a, b, n):
    if n % 2 != 0:
        raise ValueError("Число разбиений должно быть четным")
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = func(x)
    integral_sum = h / 3 * (y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-1:2]))
    return integral_sum

def example_function(x):
    return np.sin(x)

def real_integ_func(x):
    return 1 - np.cos(x)

# Задаем интервал интегрирования и количество разбиений
a = 0
b = 2 * math.pi
n = 1000  # можем увеличить количество разбиений для увеличения точности метода Симпсона

# Вычисляем интеграл используя метод прямоугольников
integral_rec = rectangle_method(example_function, a, b, n)

# Вычисляем интеграл используя метод трапеций
integral_trapezoidal = trapezoidal_method(example_function, a, b, n)

# Вычисляем интеграл используя метод Симпсона
integral_simpson = simpson_method(example_function, a, b, n)
print("Метод Симпсона:", integral_simpson)

# Реальное значение интеграла (для сравнения точности)
real_integral = np.cos(b) - np.cos(a)

# Точность метода Симпсона на интервале t
t_values = np.linspace(a, b, n+1)
accuracy_simpson_interval = example_function(t_values) - integral_simpson

# Таблица с вычисленными значениями и их точностями
data = {
    'Method': ['Rectangle', 'Trapezoidal', 'Simpson'],
    'Integral Value': [integral_rec, integral_trapezoidal, integral_simpson],
    'Accuracy': [np.abs(integral_rec - real_integral), np.abs(integral_trapezoidal - real_integral), np.abs(integral_simpson - real_integral)]
}
df = pd.DataFrame(data)
print(df)

# Создаем массив значений t
t_values = np.linspace(a, b, n+1)

# Вычисляем накопленную площадь для каждого t
cumulative_areas = []
cumulative_area = 0
for t in t_values:
    cumulative_area += rectangle_method(example_function, a, t, n)
    if example_function(t) < 0:
        cumulative_area -= example_function(t)
    cumulative_areas.append(cumulative_area)

# График накопленной площади от t
plt.plot(t_values, cumulative_areas)
plt.plot(t_values, example_function(t_values), '--', color='gray')  # Добавляем график sin(x) для сравнения
plt.xlabel('t')
plt.ylabel('Накопленная площадь')
plt.title('Накопленная площадь от t')
plt.grid(True)
plt.show()
