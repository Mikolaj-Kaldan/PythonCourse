import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dates = np.arange('2024-05-01','2024-06-01',dtype='datetime64[D]')
gold_rate = [np.random.randint(2300, 2400)]
for x in range(len(dates)-1):
    gold_rate.append(gold_rate[x]+np.random.randint(-10, 10))
series = pd.Series(data = gold_rate, index = dates)
series.plot()
plt.ylabel("Gold rate [USD/oz]")
plt.show()
