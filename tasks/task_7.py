import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

from common import data_collector

n = 350
data = data_collector(n)

bins = np.linspace(min(data), max(data), 10)

mean = np.mean(data)
std = np.std(data)

x = np.linspace(min(data), max(data), 100)
pdf = norm.pdf(x, mean, std)

plt.hist(data, bins, density=True, alpha=0.6, label='Гістограма відносних частот')
plt.plot(x, pdf, '-o', label='Нормальний розподіл')

plt.xlabel('Значення')
plt.ylabel('Відносна частота')
plt.legend()

plt.show()
