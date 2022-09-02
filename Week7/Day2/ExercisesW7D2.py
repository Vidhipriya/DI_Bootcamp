import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
# df[['Manufacturer','Make']]
make_list=df['Make'].unique().tolist()
# print(make_list)
encoded_items = df.map(lambda x: make_list[x])
pd.DataFrame({"Rank":items, "Encoded Rank":encoded_items})

means = df[['Manufacturer', 'Model']].groupby('Manufacturer').mean()
print(means)