Метод симпсона
integral_sum = 0 - это переменная, в которой будет накапливаться сумма значений функции для каждого подинтервала.

Цикл for i in range(n): перебирает все значения индексов от 0 до n-1. Здесь n - это количество подинтервалов (число разбиений).

if i == 0 or i == n: - это проверка на то, что текущий индекс i соответствует границам интервала. Если i равно 0 или n, значит это крайние точки интервала a и b. В этом случае к сумме прибавляется значение функции в точках a и b.

elif i % 2 == 0: - это проверка на четность индекса. Если индекс четный (т.е. равен 0, 2, 4, ...), значит мы находимся на четном подинтервале. В этом случае к сумме прибавляется удвоенное значение функции в текущей точке.

else: - это ветка, которая выполняется для нечетных индексов, т.е. для точек между четными подинтервалами. В этом случае к сумме прибавляется учетное значение функции в текущей точке.

integral = h / 3 * integral_sum - наконец, вычисляется окончательное значение интеграла. Мы умножаем сумму значений функции на коэффициент h/3, где h - шаг разбиения (ширина подинтервала). Этот коэффициент зависит от того, какой метод численного интегрирования мы используем (в данном случае метод Симпсона).



Надо вычислить интеграл sin(x) от 0 до t. Вычисленно решение это 1 - cos(x). mn = 20 . H = 2*pi / mn , SumInt = 0 .
И вывести график от { [0,0] , [H, интеграл от 0 до H ] , [2H , интеграл от 0 до 2H ] (Методом суммирования.