import pandas as pd

from common import data_collector, make_intervals_from_n, make_interval_labels
from const import min_value, max_value

n = 350
data = data_collector(n)

df = pd.DataFrame(data, columns=['Grades'])

bins = make_intervals_from_n(n, minimum=min_value, maximum=max_value, rounder=2)
labels = make_interval_labels(bins)
df['Grade Interval'] = pd.cut(df['Grades'], bins=bins, labels=labels)

frequency_table = df['Grade Interval'].value_counts().sort_index()

print(frequency_table)
