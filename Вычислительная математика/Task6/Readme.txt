y = |x|
1) Ашманов (Популизатор ИИ)
|x| выстроить многочлен 4 степени
2) Составляем сетку y = |x|  из 4(параметр) (то есть сетка по 4 точек) точкам (-2;2) , выстраиваем все многочлены Лагранжа. Найти такой многочлен который совпадает с точками графика y = |x| (Чтобы графики в узлах совпадали).


(*Лагранж, неопределен коэфф. Фурье, МНК*)
(*интерполяция функции*)
Plot[Abs[x], {x, -2, 2}]

pxk = {x1, x2, x3, x4};(*для теста *)
Lk = Table(*создаем все часные многочлены Лагранжа*)
ϕk = 1;
Forjj = 1, jj ≤ Length[pxk], jj++,
Ifk ⩵ jj, ϕk, ϕk = ϕk
x - pxk〚jj〛
pxk〚k〛- pxk〚jj〛
(*ϕj[x] = ∏k=1,k≠j n x-xk
xj-xk *)
; ϕk
, {k, 1, Length[pxk]}

 x - x2 x - x3 (x - x4)
x1 - x2 x1 - x3 x1 - x4
, x - x1 x - x3 (x - x4)
-x1 + x2 x2 - x3 x2 - x4
,
x - x1 x - x2 (x - x4)
-x1 + x3 -x2 + x3 x3 - x4
, x - x1 x - x2 x - x3
-x1 + x4 -x2 + x4 -x3 + x4

*================================*)
In[1]:= (*Вычисления*)
nn = 5; (*число отрезков, точек nn+1*)
pxk = Tablexk, xk, -2, 2,
4
nn
; (*точки где p[xk]=f[xk]=pfk *)
pfk = Table[Abs[pxk〚k〛], {k, 1, Length[pxk]}];
(*собираем точки для графика*)
tbpts = Table[{pxk〚k〛, Abs[pxk〚k〛]}, {k, 1, Length[pxk]}]

{{-2;2},{-6/5,6/5},{-2/5,2/5},{2/5,2/5},{6/5,6/5},{2,2}}
Show[
Plot[Abs[x], {x, -2, 2}],
ListPlot[tbpts, PlotStyle → Red]]
(Вывести график)
4]:= Lk = Table(*создаем все часные многочлены Лагранжа*)
(*pxk={x1,x2,x3,x4} для теста *)
ϕk = 1;
Forjj = 1, jj ≤ Length[pxk], jj++,
Ifk ⩵ jj, ϕk, ϕk = ϕk
x - pxk〚jj〛
pxk〚k〛- pxk〚jj〛
(*ϕj[x] = ∏k=1,k≠j n x-xk
xj-xk *); ϕk, {k, 1, Length[pxk]}
]:= PolyN = Tr[Table[Lk〚k〛 pfk〚k〛, {k, 1, Length[pxk]}]];
Show[
Plot[Abs[x], {x, -2, 2}],
ListPlot[tbpts, PlotStyle → Red],
Plot[PolyN, {x, -2, 2}]
]
(*многочлен Лагранжа через метод неопределенных коэффициентов*)
pfk = {x1, x2, x3, x4};
ϕϕL = a x3 + b x2 + c x + d;
equ = 
a x13 + b x12 + c x1 + d ⩵ 1,
a x23 + b x22 + c x2 + d ⩵ 0,
a x33 + b x32 + c x3 + d ⩵ 0,
a x43 + b x42 + c x4 + d ⩵ 0
;
Simplifya x3 + b x2 + c x + d /. Solve[equ, {a, b, c, d}]


