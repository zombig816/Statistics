import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
import numpy
import pandas as pd
from scipy. stats import norm

#считываем столбец
x = pd.read_csv("r1z1.csv")
x = numpy.array(x["X"])

# вычисляем объем выборки и размах
n = len(x)
razmah = max(x) - min(x)
print("Объём выборки:", n)
print("Размах выборки:", razmah)

# вычисляем мат.ожидание и округляем его
Mx = sum(x) / n
print("Математическое ожидание:", numpy.round(Mx, 4))

# вычисляем выборочную смещенную дисперсию
Dx_sm = (sum((x - Mx) ** 2)) / n
print("Смещенная дисперсия:", Dx_sm)


# выисляем несмещенную дисперсию
Dx_nesm = (Dx_sm * n) / (n - 1)
print("Несмещенная дисперсия:", Dx_nesm)

# вычисляем среднеквадратичное отклонение
sign = Dx_sm ** 0.5
print('Среднеквадратичное отклонение:', sign)

#медиана
x = sorted(x)
if n % 2 == 0:
    m = (x[int((n - 1) / 2)] + x[int((n - 1) / 2 + 1)]) / 2
else:
    m = (x[int((n - 1) / 2) + 1])
print('Медиана:', m)

#квартили
quartile1 = (x[int((n - 1) / 4)] + x[int((n - 1) / 4 + 1)]) / 2

quartile3 = (x[int(((n - 1) * 3) / 4)] + x[int(((n - 1) * 3) / 4 + 1)]) / 2
print(quartile1)
print(quartile3)
print(np.quantile(x, 0.25))
print(np.quantile(x, 0.75))

interquartile = quartile3 - quartile1
print('Интерквартильная широта:', interquartile)

#коэффициент асимметрии
g = (sum((x - Mx)**3)/(n * sign**3))
print(g)

# количество интервалов
k = int(n * 0.1)

# вычисляем шаг
delt = razmah / (k - 1)
print("Шаг:", delt)

a1 = min(x) + delt / 2
ak = max(x) - delt / 2

#print(a1, ak)
q = [a1]
for i in range(1, k - 2):
    q.append(q[i - 1] + delt)
q.append(q[len(q) - 1] + delt)

count_of_elems = []
count = 0

otn_count_of_elems = []

for i in x:
    if i < q[0]:
        count += 1
count_of_elems.append(count)
otn_count_of_elems.append(count/n)

for i in range(1, k - 1):
    count = 0
    for j in x:
        if q[i - 1] <= j < q[i]:
            count += 1
    count_of_elems.append(count)
    otn_count_of_elems.append(count / n)
count = 0
for i in x:
    if i > q[len(q) - 1]:
        count += 1
count_of_elems.append(count)
otn_count_of_elems.append(count/n)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots(1, 1)
fig2, ax2 = plt.subplots(1, 1)
fig3, ax3 = plt.subplots(1, 1)
fig4, ax4 = plt.subplots(1, 1)


#    частотная гистограмма

ax.plot([112, 112], [0, 0])
ax.set_xlabel('Values')
ax.set_ylabel('Occurence frequency')
ax.set_title('Frequency histogram')
ax.axvline(Mx, color='black', label='Mx')
ax.plot([m, m], [0, 30], color='blue', label='Median')

ax.add_patch(Rectangle((q[0]-delt, 0), delt, count_of_elems[0]))
for i in range(0, len(count_of_elems) - 1):
    ax.add_patch(Rectangle((q[i], 0), delt, count_of_elems[i+1]))

#   вероятностная гистограмма
ax2.plot([112, 112], [0, 0])

ax2.set_xlabel('Values')
ax2.set_ylabel('Occurence probability')
ax2.set_title('Probabilistic histogram')
ax2.axvline(Mx, color='black', label='Mx')
ax2.axvline(m, color='blue', label='Median')
ax2.axvline(quartile1, color='purple', label='Quartile 25%')
ax2.axvline(quartile3, color='grey', label='Quartile 75%')

ax2.add_patch(Rectangle((q[0]-delt, 0), delt, otn_count_of_elems[0]/delt))
for i in range(0, len(count_of_elems) - 1):
   ax2.add_patch(Rectangle((q[i], 0), delt, otn_count_of_elems[i+1]/delt))

arr = numpy.arange(110, 130, 0.001)

ax2.plot(arr, (norm. pdf(arr, Mx, sign)), color='red', label='Normal distribution')


#    полигон распределения
xx = np.arange(0, n, 1)
ax3.scatter(xx, x)


# Эмпирическая функция распределения
unic1 = list(set(x))
print(len(unic1))
unic = numpy.array(unic1)
countx = list({i: x.count(i) for i in x}.values())

print(countx)

prob = []
for i in range(0, len(countx)):
    prob.append(countx[i]/n)
print(prob)

ar2 = [sum(prob[:i+1]) for i in range(len(prob))]
ar2 = [round(item, 4) for item in ar2]
ar2 = numpy.array(ar2)
print(ar2)
print(len(ar2))

ar2 = list(ar2)
unic1 = sorted(unic1)
print(unic1[0])

print(max(x), min(x))

plt.title("Distribution function")
ax4.plot([109, unic1[0]], [0, 0], color='blue')
ax4.plot([unic1[len(unic)-1], 131], [1, 1], color='blue')
ax4.plot(unic1, ar2, color='blue', drawstyle='steps')
ax4.plot(arr, (norm. cdf(arr, Mx, sign)), color='red', label='Normal distribution')
ax.legend()
ax2.legend()
ax4.legend()
plt.show()