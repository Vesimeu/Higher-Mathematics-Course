import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

def lagrange_interpolation(x, y, x_interp):
    """
    Выполняет интерполяцию методом Лагранжа.

    Аргументы:
    x -- массив значений x для заданных точек данных
    y -- массив значений y для заданных точек данных
    x_interp -- массив значений x, в которых необходимо выполнить интерполяцию

    Возвращает:
    y_interp -- массив значений y, полученных методом интерполяции Лагранжа в точках x_interp
    """
    y_interp = np.zeros_like(x_interp)
    for i in range(len(x_interp)):
        for j in range(len(x)):
            L = 1
            # Вычисляем многочлен Лагранжа для каждой точки x_interp
            for k in range(len(x)):
                if k != j:
                    L *= (x_interp[i] - x[k]) / (x[j] - x[k])
            y_interp[i] += y[j] * L
    return y_interp

points = 9 #Количетсво точек данных
# Создаем данные для интерполяции
x_data = np.linspace(-2, 2, points)
y_data = np.abs(x_data)

# Создаем точки для интерполяции
x_interp = np.linspace(-2, 2, 100)

# Получаем значения интерполяции с использованием многочленов Лагранжа
y_interp_lagrange = lagrange_interpolation(x_data, y_data, x_interp)

# График - все частные многочлены Лагранжа
plt.figure(figsize=(8, 6))
for i in range(len(x_data)):
    l_i = lagrange_interpolation(x_data, np.eye(len(x_data))[i], x_interp)
    plt.plot(x_interp, l_i, label=f'$L_{i}(x)$')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Частные многочлены Лагранжа')
plt.legend()
plt.grid(True)
plt.show()

# График интерполяции с многочленами Лагранжа
plt.figure(figsize=(8, 6))
plt.plot(x_interp, np.abs(x_interp), label='Функция $y=|x|$')
plt.plot(x_interp, y_interp_lagrange, label='Интерполяция Лагранжа')
plt.scatter(x_data, y_data, color='red', label='Точки данных')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Интерполяция многочленами Лагранжа')
plt.legend()
plt.grid(True)
plt.show()

# Вывод отчета в консоль
data_table = list(zip(x_interp, y_interp_lagrange))
headers = ['x', 'Интерполяция Лагранжа']
print(tabulate(data_table, headers=headers, tablefmt='grid'))
