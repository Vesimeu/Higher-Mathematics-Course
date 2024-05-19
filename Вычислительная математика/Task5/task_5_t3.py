import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.integrate import solve_ivp

# Уравнение c: x'' + x = sin(t)
def equation_c(t, y):
    x, x_dot = y
    return [x_dot, np.sin(t) - x]

# Аналитическое решение для уравнения c при начальных условиях x'(0) = 0
def analytical_solution_c_0(t):
    return np.sin(t)

# Параметры для численного решения
t_span = (0, 10)  # Интервал времени
h = 0.01  # Шаг интегрирования

# Начальные условия для каждого уравнения
initial_condition_c = [0, 0]  # x'(0) = 0

# Решение уравнения c с использованием метода Рунге-Кутты четвертого порядка
solution_c = solve_ivp(equation_c, t_span, initial_condition_c, method='RK45', t_eval=np.arange(0, t_span[1], h))
t_values_c = solution_c.t
x_values_c = solution_c.y[0]
analytical_solution_c_values = analytical_solution_c_0(t_values_c)

# Функция для вычисления погрешности
def compute_error(numerical_solution, analytical_solution):
    return np.abs(numerical_solution - analytical_solution)

# Вычисление погрешности
error_c = compute_error(x_values_c, analytical_solution_c_values)

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(t_values_c, x_values_c, label='Numerical Solution (RK45)')
plt.plot(t_values_c, analytical_solution_c_values, label='Analytical Solution')
plt.title('Solution for Equation c')
plt.xlabel('Time')
plt.ylabel('x(t)')
plt.legend()
plt.grid(True)
plt.show()

# Вывод решения в виде таблицы для сравнения
solution_table_c = pd.DataFrame(
    {'t': t_values_c, 'Численное решение': x_values_c, 'Аналитическое решение': analytical_solution_c_values, 'Погрешность': error_c})
print("\nРешение для Уравнения c:")
print(solution_table_c)
