# Using pandas we will load a dataset and read that data and show only what we really need

import matplotlib.pyplot as plt
import pandas as pd

countries = pd.read_csv('countries.csv')

# Let's compare the population grow of US and China

us = countries[countries.country == 'United States']
china = countries[countries.country == 'China']

plt.plot(us.year, us.population / 10**6)
plt.plot(china.year, china.population / 10**6)
plt.legend(['United States', 'China'])
plt.xlabel('Years')
plt.ylabel('Population')
plt.show()

