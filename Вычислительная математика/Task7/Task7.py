import time
import random


def bubble_sort(arr):
    """
    Пузырьковая сортировка.

    Основная идея: Проходы по массиву, сравнение соседних элементов и их обмен,
    чтобы наибольший элемент "всплыл" в конец массива на каждом проходе.

    Параметры:
    - arr: список для сортировки
    """
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def merge_sort(arr):
    """
    Сортировка слиянием.

    Основная идея: Рекурсивное разбиение массива пополам, сортировка каждой половины
    рекурсивно, а затем слияние двух отсортированных половин в один отсортированный массив.

    Параметры:
    - arr: список для сортировки
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)  # Сортировка левой половины
        merge_sort(right_half)  # Сортировка правой половины

        # Слияние двух отсортированных половин
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def counting_sort(arr):
    """
    Сортировка подсчётом.

    Основная идея: Создание массива "счетчиков" для подсчета количества встречающихся элементов,
    а затем построение отсортированного списка на основе этих счетчиков.

    Параметры:
    - arr: список для сортировки
    """
    if isinstance(arr[0], str):  # Проверяем, является ли элемент строкой
        counts = {}
        for num in arr:
            counts[num] = counts.get(num, 0) + 1
        output = []
        for key in sorted(counts.keys()):
            output.extend([key] * counts[key])
        return output
    elif isinstance(arr[0], float):  # Проверяем, является ли элемент числом с плавающей точкой
        counts = {}
        for num in arr:
            counts[num] = counts.get(num, 0) + 1
        output = []
        for key in sorted(counts.keys()):
            output.extend([key] * counts[key])
        return output
    else:
        max_val = max(arr)
        counts = [0] * (int(max_val) + 1)
        for num in arr:
            counts[num] += 1
        output = []
        for i in range(len(counts)):
            output.extend([i] * counts[i])
        return output


# Пример использования и измерение времени выполнения каждой сортировки
# Генерация больших массивов данных
int_arr = [random.randint(1, 1000) for _ in range(10000)]
str_arr = [''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5)) for _ in range(10000)]
float_arr = [random.uniform(0, 1000) for _ in range(10000)]

# Пример использования и измерение времени выполнения каждой сортировки
arrays = {
    "int": int_arr,
    "string": str_arr,
    "float": float_arr
}

sorting_algorithms = {
    "Bubble Sort": bubble_sort,
    "Merge Sort": merge_sort,
    "Counting Sort": counting_sort,
}

for data_type, arr in arrays.items():
    print(f"Тип данных: {data_type}")
    for sort_name, sort_func in sorting_algorithms.items():
        start_time = time.time()
        sorted_arr = arr.copy()
        sort_func(sorted_arr)
        end_time = time.time()
        print(f"{sort_name}: Время выполнения - {end_time - start_time:.6f} секунд")
    print()

# 1)Пузырьковая сортировка - простая в реализации, но неэффективна на больших данных из-за квадратичной сложности.
#
# 2)Сортировка слиянием - эффективна на больших данных и имеет стабильную
# производительность на разных типах данных,
# но требует дополнительной памяти.
#
# 3)Сортировка подсчётом - эффективна на маленьких данных и
# в особенности на данных с ограниченным диапазоном значений,
# но может быть неэффективна при большом разнообразии значений или большом диапазоне значений.