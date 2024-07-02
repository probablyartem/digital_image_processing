import numpy as np
import matplotlib.pyplot as plt
import math


x1 = np.linspace(0.0, 15.0, 100)
y1 = 0.3*10*x1+10*10
noize = np.random.normal(0,0.5,100)
plt.plot(x1, y1+noize)
plt.plot(x1, y1)
plt.title('Функция #1')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()

x2 = np.linspace(0.0, 15.0, 100)
y2 = np.cos(0.5*10*x2)+10*np.sin(x2+10)

plt.plot(x2, y2+noize)
plt.plot(x2, y2)
plt.title('Функция #2')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()

x3 = np.linspace(0.0, 15.0, 100)
y3 = 10*np.cos(2*np.pi*x3)*np.exp(-0.1*10*x3)

plt.plot(x3, y3+noize)
plt.plot(x3, y3)
plt.title('Функция #3')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()


y = [y1, y2, y3]



def my_max(y_):
    # n, = y.shape
    maxim = y_[0]
    for i in y_:
        if i > maxim:
            maxim = i
    return maxim

def my_min(y_):
    # n,  = y.shape
    minim = y_[0]
    for i in y_:
        if i < minim:
            minim = i
    return minim

def my_average(y_):
    # n,  = y.shape
    summ = 0
    num = 0
    for i in y_:
        summ += i
        num += 1
    return summ / num

def my_median(y_):
    n, = y_.shape
    sort_arr = np.sort(y_)
    if n % 2 == 0:
        return (sort_arr[n // 2 - 1] + sort_arr[n // 2]) / 2
    else:
        return sort_arr[n // 2]
    
def my_std(y_):
    aver = my_average(y_)
    n, = y_.shape
    summ = 0
    for i in y_:
        summ += (i - aver) ** 2
    return np.sqrt(summ / n)




np_data = [
    [np.amax(y_) for y_ in y],
    [np.amin(y_) for y_ in y],
    [np.average(y_) for y_ in y],
    [np.median(y_) for y_ in y],
    [np.std(y_) for y_ in y]]



my_data = [
    [my_max(y_) for y_ in y],
    [my_min(y_) for y_ in y],
    [my_average(y_) for y_ in y],
    [my_median(y_) for y_ in y],
    [my_std(y_) for y_ in y]]


xlim = [15, 11, 5]
fig = plt.figure(figsize=(10, 10))
fig.suptitle('Графики заданных функций', fontsize=15, fontweight='bold')
for i in range(3):
    if i != 2:
        ax = fig.add_subplot(2, 2, i + 1)
    else:
        ax = fig.add_subplot(2, 1, i)
    
    ax.plot(x1, y[i], linewidth=2, label=f'График y{i + 1}')
    # ax.set_title(f'График y{i+1}')
    ax.legend(loc='upper right')
    ax.grid()
    ax.set_xlim((0, xlim[i]))
    ax.set_xlabel('x')
    ax.set_ylabel('y')
plt.show()

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





# print('для функции №1\n',np.amax(y1), np.amin(y1), np.average(y1), np.median(y1), np.std(y1))

# print(max(y1), min(y1), mean(y1), median(y1), stdev(y1),'\n')

# print('для функции №2\n',np.amax(y2), np.amin(y2), np.average(y2), np.median(y2), np.std(y2))

# print(max(y2), min(y2), mean(y2), median(y2), stdev(y2),'\n')

# print('для функции №3\n',np.amax(y3), np.amin(y3), np.average(y3), np.median(y3), np.std(y3))

# print(max(y3), min(y3), mean(y3), median(y3), stdev(y3),'\n')
