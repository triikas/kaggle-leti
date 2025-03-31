import numpy as np
import matplotlib.pyplot as plt

# Определение функции δ_1(t)
def delta_1(t):
    return (t >= 0).astype(float)

# Определение основной функции
def f(t):
    term1 = np.exp(-t/2) * np.sin(t/2) * delta_1(t)
    term2 = -np.exp(10) * np.sin((10 - t/2)) * delta_1(t - 20)
    term3 = 2 * np.exp(5) * np.sin((5 - t/2)) * delta_1(t - 10)
    return (1/10) * (term1 + term2 + term3)

# Период сигнала
T = 40

# Создание массива значений t
t = np.linspace(0, T, 1000)  # Измените диапазон и количество точек по необходимости

# Вычисление значений функции с учетом периодичности
y = np.array([f(ti % T) for ti in t])

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(t, y, label='$f(t)$')
plt.title('График функции $f(t)$ с периодом 40')
plt.xlabel('$t$')
plt.ylabel('$f(t)$')
plt.legend()
plt.grid(True)
plt.show()
