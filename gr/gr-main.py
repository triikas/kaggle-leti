import math

import matplotlib.pyplot as plt
import numpy as np

# Создаём экземпляр класса figure и добавляем к Figure область Axes
fig, ax = plt.subplots()


x = np.linspace(0, 40, 100) # X от -5 до 5

y = (x**2)/((4*(x**4)+1)**0.5)
# print(max(y))
# y0 = x*0 + 1
# y = (-np.arctan(2 * x / (1 - 2 * x**2))) * (x <= (2**0.5) / 2) + (-np.pi + np.arctan(2 * x / (1 - 2 * x**2))) * (x > (2**0.5) / 2)
# y = (np.degrees(np.pi) - np.degrees(np.arctan2(2 * x, (1 - 2 * x**2))))
# y = (2/40)*(np.sqrt(((-1+2*np.cos(10*x)-np.cos(20*x))/(10*x**2))**2+((np.sin(20*x)-2*np.sin(10*x))/(10*x**2))**2))
# y = (x/10)*(x>=0)-((2*x-20)/10)*(x>=10)+((x-20)/10)*(x>=20)
# y = (1/20)*(np.sqrt(((-1+2*np.cos(10*x)-np.cos(20*x))/(10*x**2))**2+((np.sin(20*x)-2*np.sin(10*x))/(10*x**2))**2))*((x**2)/((4*(x**4)+1)**0.5))
# y = np.arctan2((np.sin(20*x)-2*np.sin(10*x)), (-1+2*np.sin(10*x)-np.cos(20*x)))
# y = np.arctan2((np.sin(20*x)-2*np.sin(10*x)), (-1+2*np.sin(10*x)-np.cos(20*x))) + (np.pi - np.arctan2(2 * x, (1 - 2 * x**2)))
# y = 0.1*np.exp(-x/2)*( np.sin(x/2)*(x>=0) - np.exp(10)*np.sin(10-(x/2))*(x>=20) + 2*np.exp(5)*np.sin(5-(x/2))*(x>=10) )
# y = (-x**2)/(2*np.i)
xx = np.array([])
for i in range(1, 18):
    # if i == 2 or i == 6 or i == 10:
    #     continue
    xx = np.append(xx, 0.157*i)
# yy = (2/40)*(np.sqrt(((-1+2*np.cos(10*xx)-np.cos(20*xx))/(10*xx**2))**2+((np.sin(20*xx)-2*np.sin(10*xx))/(10*xx**2))**2))
# yy = np.arctan2((np.sin(20*xx)-2*np.sin(10*xx)), (-1+2*np.sin(10*xx)-np.cos(20*xx)))
# yy = (1/20)*(np.sqrt(((-1+2*np.cos(10*xx)-np.cos(20*xx))/(10*xx**2))**2+((np.sin(20*xx)-2*np.sin(10*xx))/(10*xx**2))**2))*((xx**2)/((4*(xx**4)+1)**0.5))
yy = np.arctan2((np.sin(20*xx)-2*np.sin(10*xx)), (-1+2*np.sin(10*xx)-np.cos(20*xx))) + (np.pi - np.arctan2(2 * xx, (1 - 2 * xx**2)))
ax.plot(x, y)
print(yy)
# for x1, y1 in zip(xx, yy):
#     plt.axvline(x=x1,ymax=0.4, color='b', linestyle='--')
#     print(y1)
#     plt.scatter(x1, y1, color='r')
def piecewise_signal(x):
    return ((x/10) * (x >= 0) - ((2*x - 20)/10) * (x >= 10) + ((x - 20)/10) * (x >= 20))

# # Период сигнала
# T = 40
#
# # Создание массива значений x
# x = np.linspace(0, 3*T, 1000)
#
# # Вычисление значений сигнала с учетом периодичности
# y = piecewise_signal(x % T)
#
# # Построение графика
# plt.figure(figsize=(10, 6))
# plt.plot(x, y, label='Piecewise Signal')
def i_1(t):
    return (9.97991703e-03 * np.cos(0.157 * (t+11) - 0.79) +
            1.96221255e-02 * np.cos(2 * 0.157 * (t+11) + 2.03759042) +
            9.16253710e-03 * np.cos(3 * 0.157 * (t+11) + -0.66063595) +
            3.98314493e-08 * np.cos(4 * 0.157 * (t+11) + 4.45925826) +
            6.27565475e-03 * np.cos(5 * 0.157 * (t+11) + 4.8790081) +
            9.81796065e-03 * np.cos(6 * 0.157 * (t+11) + 0.64039554))

# Создание массива значений t
t = np.linspace(0, 40, 1000)  # Измените диапазон и количество точек по необходимости

# Вычисление значений i_1(t)
i1_values = i_1(t)

# Построение графика
# plt.figure(figsize=(10, 6))
# plt.plot(t, i1_values, label='$i_1(t)$', color='b')
for x1, y1 in zip(xx, yy):
    fx = np.array([x1, x1])
    fy = np.array([y1, 0])
    # ax.plot(fx, fy)
plt.show()
# ------------------------------------------------------------------------
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Создаем массив частот от 0.1 Гц до 100 Гц (в логарифмическом масштабе)
# frequencies = np.logspace(-1, 2, 500)


# # Функция для расчета фазы
# def phase_response_custom(frequencies):
#     # В числителе -omega^2 (фаза 180 градусов)
#     num_phase = np.pi
#
#     # В знаменателе 2jω - 2ω^2 + 1 (фаза определяется арктангенсом)
#     den_phase = np.arctan2(2 * frequencies, 1 - 2 * frequencies ** 2)
#
#     # Общая фаза H(jω) = π - arctan(...)
#     total_phase = num_phase - den_phase
#
#     # Конвертация в градусы
#     return np.degrees(total_phase)
#
#
# # Расчет фазового отклика для заданной передаточной функции
# custom_phase = phase_response_custom(frequencies)
#
# # Создание графика
# plt.figure(figsize=(10, 6))
# plt.semilogx(frequencies, custom_phase, label='ФЧХ для H(jω) = -ω² / (2jω - 2ω² + 1)')
# plt.xlabel('Частота (Гц)')
# plt.ylabel('Фаза (градусы)')
# plt.title('Фазочастотная характеристика (ФЧХ)')
# plt.axhline(0, color='grey', lw=0.5, linestyle='--')
# plt.grid(True, which='both', linestyle='--', linewidth=0.5)
# plt.legend()
# plt.show()
# --------------------------------------------------------
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Определение ОЧХ
# def H(w):
#     return -w**2 / (2j*w - 2*w**2 + 1)
#
# # Модуль ОЧХ
# def abs_H(w):
#     return np.abs(H(w))
#
# # Фаза ОЧХ
# def angle_H(w):
#     return np.angle(H(w))
#
# # Создание массива частот
# w = np.linspace(0.01, 10, 1000)
#
# # Вычисление модуля и фазы
# abs_values = abs_H(w)
# phase_values = angle_H(w)
#
# # Построение графика
# plt.figure(figsize=(10, 5))
#
# # График модуля
# plt.subplot(2, 1, 1)
# plt.plot(w, abs_values)
# plt.title('Амплитудно-частотная характеристика')
# plt.xlabel('Частота')
# plt.ylabel('Амплитуда')
#
# # График фазы
# plt.subplot(2, 1, 2)
# plt.plot(w, phase_values)
# plt.title('Фазовая характеристика')
# plt.xlabel('Частота')
# plt.ylabel('Фаза')
#
# plt.tight_layout()
# plt.show()
# -----------------------------------------------------
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Определение функции
# def H(omega):
#     return -omega**2 / (2j * omega - 2 * omega**2 + 1)
#
# # Создание массива значений ω
# omega = np.linspace(0, 1000, 100000)
#
# # Вычисление значений функции для каждого ω
# H_values = H(omega)
#
# # Построение графика на комплексной плоскости
# plt.figure(figsize=(8, 6))
# plt.plot(H_values.real, H_values.imag)
# # plt.title('График комплексной функции')
# plt.xlabel('Re')
# plt.ylabel('Im')
# plt.grid(True)
# plt.show()

