import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

# ITS PRINT
def print_difference_table_all_derivatives(x_values, dfL_values, dfR_values, dfLR_values, g_values):
    # Вычисление разности между значениями dfL(x), dfR(x), dfLR(x) и g(x)
    difference_dfL = abs(dfL_values - g_values)
    difference_dfR = abs(dfR_values - g_values)
    difference_dfLR = abs(dfLR_values - g_values)

    # Подготовка данных для таблицы
    data = {"x": x_values, "dfL(x)": dfL_values, "dfR(x)": dfR_values, "dfLR(x)": dfLR_values, "g(x)": g_values,
            "Разность (dfL - g)": difference_dfL, "Разность (dfR - g)": difference_dfR,
            "Разность (dfLR - g)": difference_dfLR}
    table = []
    for i in range(len(x_values)):
        row = [x_values[i], dfL_values[i], dfR_values[i], dfLR_values[i], g_values[i], difference_dfL[i],
               difference_dfR[i], difference_dfLR[i]]
        table.append(row)

    # Вывод таблицы с помощью tabulate
    headers = ["x", "dfL(x)", "dfR(x)", "dfLR(x)", "g(x)", "Разность (dfL - g)", "Разность (dfR - g)",
               "Разность (dfLR - g)"]
    print(tabulate(table, headers=headers, floatfmt=".10f", tablefmt="pretty"))

# Определение функций f(x) и g(x)
def f(x):
    return np.sin(x)

def g(x):
    return np.cos(x)

# Метод численного дифференцирования: левая разность
def numerical_diff_left(f, x, h):
    return (f(x) - f(x - h)) / h

# Метод численного дифференцирования: правая разность
def numerical_diff_right(f, x, h):
    return (f(x + h) - f(x)) / h

# Метод численного дифференцирования: центральная разность
def numerical_diff_central(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

# Определение точек и шага
x_values = np.linspace(0, 2*np.pi, 100)
print(x_values)
# h = x_values[1] - x_values[0]
h = 10**(-8)

# Вычисление производных
dfL = [numerical_diff_left(f, x, h) for x in x_values]
dfR = [numerical_diff_right(f, x, h) for x in x_values]
dfLR = [numerical_diff_central(f, x, h) for x in x_values]

# Аналитические значения производной g(x) = cos(x)
dg = g(x_values)

print_difference_table_all_derivatives(x_values, dfL, dfR, dfLR, g(x_values))

# Расчет точности
accuracy_dfL = np.mean(np.abs(dfL - dg))
accuracy_dfR = np.mean(np.abs(dfR - dg))
accuracy_dfLR = np.mean(np.abs(dfLR - dg))

print("Точность (среднее абсолютное отклонение):")
print("Левая разность:", accuracy_dfL)
print("Правая разность:", accuracy_dfR)
print("Центральная разность:", accuracy_dfLR) # более точное

# Построение графиков
plt.figure(figsize=(10, 6))
# plt.plot(x_values, dfL, label="dfL")
# plt.plot(x_values, dfL - dg, label="dfL - g")
# plt.plot(x_values, dfR, label="dfR")
# plt.plot(x_values, dfR - dg, label="dfR - g")
plt.plot(x_values, dfLR - dg, label="dfLR - g")
plt.xlabel("x")
plt.ylabel("Значение производной")
plt.title("Численное дифференцирование")
plt.legend()
plt.grid(True)
plt.show()
