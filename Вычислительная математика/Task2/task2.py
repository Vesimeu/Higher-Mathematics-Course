import math

# Функция, представляющая уравнение f(x) = x^2 - 2.
def f(x):
    """Вычисляет значение функции f(x) = x^2 - 2."""
    return x**2 - 2

# Производная функции f(x), используется в методе Ньютона.
def f_prime(x):
    """Вычисляет значение производной функции f'(x) = 2x."""
    return 2*x

# Метод дихотомии для нахождения корня уравнения на заданном интервале.
def bisection_method(a, b, tol):
    """
    Использует метод дихотомии (бисекции) для нахождения корня функции на интервале [a, b].
    Предполагается, что функция имеет разные знаки на концах интервала.

    """
    if f(a) * f(b) >= 0:
        print("Ошибка: Функция должна иметь разные знаки на концах интервала [a, b].")
        return None

    while (b - a) / 2.0 > tol:
        c = (a + b) / 2.0  # Вычисляем середину текущего интервала
        if f(c) == 0:
            break  # Нашли точный корень
        elif f(a) * f(c) < 0:
            b = c  # Корень находится в левой половине интервала
        else:
            a = c  # Корень находится в правой половине интервала
    return (a + b) / 2.0  # Возвращаем среднее значение интервала как приближение к корню


# Метод простых итераций с заданной функцией phi.
def simple_iteration(phi, x0, tol, max_iter=1000):
    """
    Использует метод простых итераций для нахождения корня уравнения.
    Функция phi должна быть выбрана так, чтобы обеспечить сходимость.

    """
    for _ in range(max_iter):
        x1 = phi(x0)  # Вычисляем следующее приближение к корню
        if abs(x1 - x0) < tol:  # Проверяем, удовлетворяет ли разница между приближениями заданной точности
            return x1
        x0 = x1
    print("Превышено максимальное количество итераций для метода простых итераций.")
    return x1  # Возвращаем последнее вычисленное приближение к корню


# Метод Ньютона для нахождения корня уравнения.
def newton_method(f, f_prime, x0, tol):
    """
    Использует метод Ньютона (касательных) для нахождения корня функции.
    Начинает с начального приближения x0 и итеративно уточняет корень.

    """
    while True:
        x1 = x0 - f(x0) / f_prime(x0)  # Итерационная формула метода Ньютона
        if abs(x1 - x0) < tol:  # Проверка сходимости к корню
            break
        x0 = x1
    return x1  # Возвращаем найденное приближение к корню


# Интервалы и начальные приближения для методов
a_pos, b_pos = 1, 2  # Интервал для поиска sqrt(2)
a_neg, b_neg = -2, -1  # Интервал для поиска -sqrt(2)
x0_pos, x0_neg = 1.5, -1.5  # Начальные приближения
tol = 1e-6  # Точность

# Вычисление корней
root_bisection_pos = bisection_method(a_pos, b_pos, tol)
root_bisection_neg = bisection_method(a_neg, b_neg, tol)
phi = lambda x: (x + 2/x) / 2  # Функция для метода простых итераций
root_simple_iteration_pos = simple_iteration(phi, x0_pos, tol)
root_simple_iteration_neg = simple_iteration(phi, x0_neg, tol)
root_newton_pos = newton_method(f, f_prime, x0_pos, tol)
root_newton_neg = newton_method(f, f_prime, x0_neg, tol)

# Вывод результатов
print(f"Корень методом дихотомии: {root_bisection_pos} (положительный), {root_bisection_neg} (отрицательный)")
print(f"Корень методом простых итераций: {root_simple_iteration_pos} (положительный), {root_simple_iteration_neg} (отрицательный)")
print(f"Корень методом Ньютона: {root_newton_pos} (положительный), {root_newton_neg} (отрицательный)")

# Проверка корректности найденных корней с известным значением sqrt(2)
sqrt_2 = math.sqrt(2)
print(f"Проверка корректности корней с sqrt(2):")
print(f"Дихотомия (положительный): {math.isclose(root_bisection_pos, sqrt_2, rel_tol=1e-6)}")
print(f"Дихотомия (отрицательный): {math.isclose(root_bisection_neg, -sqrt_2, rel_tol=1e-6)}")
print(f"Простые итерации (положительный): {math.isclose(root_simple_iteration_pos, sqrt_2, rel_tol=1e-6)}")
print(f"Простые итерации (отрицательный): {math.isclose(root_simple_iteration_neg, -sqrt_2, rel_tol=1e-6)}")
print(f"Ньютон (положительный): {math.isclose(root_newton_pos, sqrt_2, rel_tol=1e-6)}")
print(f"Ньютон (отрицательный): {math.isclose(root_newton_neg, -sqrt_2, rel_tol=1e-6)}")