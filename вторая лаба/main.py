import matplotlib.pyplot as plt
import numpy
import pandas

#считываем столбец
df = pandas.read_csv("r4z2.csv")
x = df['X'].values
y = df['Y'].values

n = len(x)
# вычисляем мат.ожидание и округляем его
Mx = sum(x) / n
print("Математическое ожидание x:", numpy.round(Mx, 4))
My = sum(y) / n
print("Математическое ожидание y:", numpy.round(My, 4))

# вычисляем выборочную смещенную дисперсию
Dx_sm = (sum((x - Mx) ** 2)) / n
print("Смещенная дисперсия x:", numpy.round(Dx_sm, 4))
Dy_sm = (sum((y - My) ** 2)) / n
print("Смещенная дисперсия y:", numpy.round(Dy_sm, 4))

# выисляем несмещенную дисперсию
Dx_nesm = (Dx_sm * n) / (n - 1)
print("Несмещенная дисперсия x:", numpy.round(Dx_nesm, 4))
Dy_nesm = (Dy_sm * n) / (n - 1)
print("Несмещенная дисперсия y:", numpy.round(Dy_nesm, 4))

# вычисляем среднеквадратичное отклонение
sigmx = Dx_sm ** 0.5
print('Среднеквадратичное отклонение x:', numpy.round(sigmx, 4))
sigmy = Dy_sm ** 0.5
print('Среднеквадратичное отклонение y:', numpy.round(sigmy, 4))

# коэфф корреляции
corr = sum((x - Mx)*(y - My))/(n * sigmx * sigmy)
print("Коэффициент корреляции:", numpy.round(corr, 4))

# коэффициент регрессии
bxy = (corr * sigmx)/sigmy
print("Коэффициент регрессии:", numpy.round(bxy, 4))

print("Общий вид уравнения регрессии: x =", numpy.round(Mx, 4), "+", numpy.round(bxy,4), "* (y -", numpy.round(My,4), ")")

regr = []
prognoz = []
for i in range(len(x)):
    regr.append(Mx + bxy * (y[i] - My))
for i in range(len(x)):
    prognoz.append(Mx + bxy * (78 - My))
print("Прогноз для Х при Y=82 =", prognoz[0])

# строим регрессию Х на У при У = 78
fig, ax = plt.subplots(1, 1)
ax.scatter(x, y)
ax.plot(regr, y, color='blue', label='Линейная регрессия Х на Y')
ax.plot(prognoz, y, color='red', label='Прогноз для Х при Y = 78')
plt.legend()
plt.show()