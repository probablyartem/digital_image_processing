import numpy as np
import matplotlib.pyplot as plt


# Функция поиска максимума вектора для значений
def my_max(y_):
    # n, = y.shape
    maxim = y_[0]
    for i in y_:
        if i > maxim:
            maxim = i
    return maxim


# Функция поиска минимума для вектора значений
def my_min(y_):
    # n,  = y.shape
    minim = y_[0]
    for i in y_:
        if i < minim:
            minim = i
    return minim


# Функция поиска среднего значения для вектора значений
def my_average(y_):
    # n,  = y.shape
    summ = 0
    num = 0
    for i in y_:
        summ += i
        num += 1
    return summ / num


# Функция поиска медианного значения для вектора значений
def my_median(y_):
    n, = y_.shape
    sort_arr = np.sort(y_)
    if n % 2 == 0:
        return (sort_arr[n // 2 - 1] + sort_arr[n // 2]) / 2
    else:
        return sort_arr[n // 2]


# Функция поиска среднеквадратичного значения для вектора значений
def my_std(y_):
    aver = my_average(y_)
    n, = y_.shape
    summ = 0
    for i in y_:
        summ += (i - aver) ** 2
    return np.sqrt(summ / n)


# Функция округления полученных результатов
def round_answ(answ_, accuracy_=0):
    for line in range(len(answ_)):
        for value in range(len(answ_[0])):
            answ_[line][value] = round(answ_[line][value], accuracy_)
    return answ_


# Номер варианта
N = 12  

# Аргумент функций
x = np.linspace(0, 15, 100)

# Функции
y1 = 0.3 * N * x + 10 * N
y2 = np.cos(0.5 * N * x) + N * np.sin(x + N)
y3 = N * np.cos(2 * np.pi * x) * np.exp(-0.1 * N * x)

# Массив, содержащий значения всех функций
y = [y1, y2, y3]

# Массив с ограничениями по оси абсцисс
xlim = [15, 11, 5]

# Вывод каждой функции
for i in range(len(y)):
    plt.plot(x, y[i])
    plt.title(f'График y{i+1}', fontsize=15, fontweight='bold')
    plt.grid()
    plt.xlim((0, xlim[i]))
    plt.xlabel('x', fontsize=15, fontweight='bold')
    plt.ylabel('y',  fontsize=15, fontweight='bold')
    plt.show()

# Массив шума, содержащий значения [0, 1)
noise = np.random.rand(y1.shape[0], )

# Добавление шума к значениям функций
y = [y_ + noise for y_ in y]

# Вывод каждой функции
for i in range(len(y)):
    plt.plot(x, y[i])
    plt.title(f'График y{i+1}', fontsize=15, fontweight='bold')
    plt.grid()
    plt.xlim((0, xlim[i]))
    plt.xlabel('x', fontsize=15, fontweight='bold')
    plt.ylabel('y',  fontsize=15, fontweight='bold')
    plt.show()

# Вывод всех функций на одном листе
fig = plt.figure(figsize=(10, 10))
fig.suptitle('Графики заданных функций', fontsize=15, fontweight='bold')
for i in range(3):
    if i != 2:
        ax = fig.add_subplot(2, 2, i + 1)
    else:
        ax = fig.add_subplot(2, 1, i)
    
    ax.plot(x, y[i], linewidth=2, label=f'График y{i + 1}')
    # ax.set_title(f'График y{i+1}')
    ax.legend(loc='upper right')
    ax.grid()
    ax.set_xlim((0, xlim[i]))
    ax.set_xlabel('x')
    ax.set_ylabel('y')
plt.show()

# Массив с максимальными, минимальными, средними, 
# медианными и среднеквадратичными значениями для всех функций, 
# полученных с помощью библиотеки numpy
np_data = [
    [np.amax(y_) for y_ in y],
    [np.amin(y_) for y_ in y],
    [np.average(y_) for y_ in y],
    [np.median(y_) for y_ in y],
    [np.std(y_) for y_ in y]]

# Массив с максимальными, минимальными, средними, 
# медианными и среднеквадратичными значениями для всех функций, 
# полученных с помощью написанных с применением 
# стандартных конструкций python функций
my_data = [
    [my_max(y_) for y_ in y],
    [my_min(y_) for y_ in y],
    [my_average(y_) for y_ in y],
    [my_median(y_) for y_ in y],
    [my_std(y_) for y_ in y]]

# Вывод результата
print('------------------------------------------------------------------------')
print(
    f'Для последовательностей y1, y2, y3 с использованием numpy определены:',
    f'Максимальное значение: {np_data[0][0]:.3f}, {np_data[0][1]:.3f}, {np_data[0][2]:.3f}',
    f'Минимальное значение: {np_data[1][0]:.3f}, {np_data[1][1]:.3f}, {np_data[1][2]:.3f}',
    f'Среднее значение: {np_data[2][0]:.3f}, {np_data[2][1]:.3f}, {np_data[2][2]:.3f}',
    f'Медианное значение: {np_data[3][0]:.3f}, {np_data[3][1]:.3f}, {np_data[3][2]:.3f}',
    f'Среднеквадратичное значение: {np_data[4][0]:.3f}, {np_data[4][1]:.3f}, {np_data[4][2]:.3f}',
    sep='\n'
)
print('------------------------------------------------------------------------')
print(
    f'Для последовательностей y1, y2, y3 с использованием написанных функций:',
    f'Максимальное значение: {my_data[0][0]:.3f}, {my_data[0][1]:.3f}, {my_data[0][2]:.3f}',
    f'Минимальное значение: {my_data[1][0]:.3f}, {my_data[1][1]:.3f}, {my_data[1][2]:.3f}',
    f'Среднее значение: {my_data[2][0]:.3f}, {my_data[2][1]:.3f}, {my_data[2][2]:.3f}',
    f'Медианное значение: {my_data[3][0]:.3f}, {my_data[3][1]:.3f}, {my_data[3][2]:.3f}',
    f'Среднеквадратичное значение: {my_data[4][0]:.3f}, {my_data[4][1]:.3f}, {my_data[4][2]:.3f}',
    sep='\n'
)
print('------------------------------------------------------------------------')
