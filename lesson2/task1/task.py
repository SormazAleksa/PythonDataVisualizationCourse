# So our task is to use matplotlib and pandas to import dataset with most popular games on different platform
# First we want to import libs

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

fdata = pd.read_csv("dataset.csv")

# Now we want to show data only for PS, XOne, PC and WiiU in this order

fdata_filtered = fdata[['platform', 'genre']].dropna(subset=['platform', 'genre'])
fdata_filtered = fdata_filtered[fdata_filtered['platform'].isin(['PS4', 'XOne', 'PC', 'WiiU'])]

# Define platform order
porder = ['PS4', 'XOne', 'PC', 'WiiU']

# Create count plot
plt.figure(figsize=(12, 6))
sns.set_style('darkgrid')
sns.countplot(x='platform', hue='genre', data=fdata_filtered, palette='tab20', order=porder)

# Set title and labels for better readability
plt.title('Number of games per Genre by Platform')
plt.ylabel('Number of Games')
plt.xlabel('Platform')
plt.xticks(rotation=0)
plt.legend(title='Genre', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# Show the plot
plt.show()
