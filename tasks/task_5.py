import matplotlib.pyplot as plt
import numpy as np

from common import data_collector, make_intervals_from_n
from const import max_value, min_value

n = 350

data = data_collector(n)

bins = make_intervals_from_n(n, maximum=max_value, minimum=min_value, rounder=1)

hist, _ = np.histogram(data, bins=bins)
relative_frequencies = hist / np.sum(hist)

plt.bar(range(len(relative_frequencies)), relative_frequencies,
        tick_label=[f"{i}-{j}" for i, j in zip(bins[:-1], bins[1:])])

plt.xlabel('Інтервали')
plt.ylabel('Відносна частота')
plt.xticks(rotation=30)

plt.show()
