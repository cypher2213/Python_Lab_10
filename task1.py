import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 4, 400)

y = 5 * np.sin(10 * x) * np.sin(3 * x)


plt.figure(figsize=(8, 4))
plt.plot(x, y, linestyle='solid', linewidth=2, color='blue', label='Y(x) = 5*sin(10x)*sin(3x)')

plt.xlabel('x')
plt.ylabel('Y(x)')
plt.title('Графік функції Y(x)')

plt.legend()

plt.grid(True)


plt.show()
