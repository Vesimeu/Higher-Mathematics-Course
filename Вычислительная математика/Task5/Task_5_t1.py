import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Функция для решения дифференциального уравнения методом Тейлора
def solve_taylor_method(f, initial_condition, h, t_end):
    t_values = np.arange(0, t_end, h)
    x_values = np.zeros_like(t_values)
    x_dot_values = np.zeros_like(t_values)

    # Устанавливаем начальные условия
    x_values[0] = initial_condition[0]
    x_dot_values[0] = initial_condition[1]

    for i in range(1, len(t_values)):
        x = x_values[i - 1]
        x_dot = x_dot_values[i - 1]
        x_ddot = f(x, x_dot, t_values[i])

        # Вычисляем новые значения x и x'
        x_values[i] = x + h * x_dot + (h ** 2) / 2 * x_ddot
        x_dot_values[i] = x_dot + h * x_ddot

    return t_values, x_values, x_dot_values


# Уравнение a: x''(t) + x(t) = 0
def equation_a(x, x_dot, t):
    return -x


# Аналитическое решение для уравнения a
def analytical_solution_a(t):
    return np.cos(t) + np.sin(t)


# Уравнение b: x'' + x = t
def equation_b(x, x_dot, t):
    return t - x


# Аналитическое решение для уравнения b при начальных условиях x(0) = 0 и x'(0) = 0
def analytical_solution_b_0_0(t):
    return t - 1 + np.exp(-t)


# Уравнение c: x'' + x = sin(t)
def equation_c(x, x_dot, t):
    return np.sin(t) - x


# Аналитическое решение для уравнения c при начальных условиях x'(0) = 0
def analytical_solution_c_0(t):
    return (1 - np.exp(-t)) * np.sin(t)


# Функция для вычисления погрешности
def compute_error(numerical_solution, analytical_solution):
    return np.abs(numerical_solution - analytical_solution)


# Функция для построения графиков
def plot_solution(t_values, numerical_solution, analytical_solution, error):
    plt.figure(figsize=(12, 4))
    plt.subplot(1, 2, 1)
    plt.plot(t_values, numerical_solution, label='Numerical Solution')
    plt.plot(t_values, analytical_solution, label='Analytical Solution')
    plt.title('Solution')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(t_values, error, label='Error')
    plt.title('Error')
    plt.legend()

    plt.show()


# Параметры для численного решения
h = 0.01  # Шаг интегрирования
t_end = 10  # Конечное время

# Начальные условия для каждого уравнения
initial_condition_a = [1, 1]  # x(0) = 1, x'(0) = 1
initial_condition_b = [0, 1]  # x(0) = 0, x'(0) = 0
initial_condition_c = [0, 0]  # x'(0) = 0

# Решение уравнения a
t_values_a, x_values_a, _ = solve_taylor_method(equation_a, initial_condition_a, h, t_end)
error_a = compute_error(x_values_a, analytical_solution_a(t_values_a))

# Решение уравнения b
t_values_b, x_values_b, _ = solve_taylor_method(equation_b, initial_condition_b, h, t_end)
error_b = compute_error(x_values_b, analytical_solution_b_0_0(t_values_b))

# Решение уравнения c
t_values_c, x_values_c, _ = solve_taylor_method(equation_c, initial_condition_c, h, t_end)
error_c = compute_error(x_values_c, analytical_solution_c_0(t_values_c))

# Построение графиков
plot_solution(t_values_a, x_values_a, analytical_solution_a(t_values_a), error_a)
plot_solution(t_values_b, x_values_b, analytical_solution_b_0_0(t_values_b), error_b)
plot_solution(t_values_c, x_values_c, analytical_solution_c_0(t_values_c), error_c)

# Вывод решения в виде таблицы для сравнения
solution_table_a = pd.DataFrame(
    {'t': t_values_a, 'Численное решение': x_values_a, 'Аналитическое решение': analytical_solution_a(t_values_a)})
print("Решение для Уравнения a:")
print(solution_table_a)

solution_table_b = pd.DataFrame(
    {'t': t_values_b, 'Численное решение': x_values_b, 'Аналитическое решение': analytical_solution_b_0_0(t_values_b)})
print("\nРешение для Уравнения b:")
print(solution_table_b)

solution_table_c = pd.DataFrame(
    {'t': t_values_c, 'Численное решение': x_values_c, 'Аналитическое решение': analytical_solution_c_0(t_values_c)})
print("\nРешение для Уравнения c:")
print(solution_table_c)
