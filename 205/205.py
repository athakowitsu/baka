from re import X
from turtle import color
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import csv

with open('./SeoulBikeData.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')  
    print(reader)
    for i in reader:

        print(i)
             




sns.set_theme(style="whitegrid")

# Load the example diamonds dataset
diamonds = sns.load_dataset("diamonds")


import seaborn as sns
sns.set_theme()

labels = ['Rented Bike Count', 'Hour', 'Tempreature', 'Humidity'
]

reader.plot(reader.corr(),
xticklabels=labels,
yticklabels=labels)
plt.show()







# sns.heatmap(reader.corr(),
# annot=True,
# cmap='Reds',
# xticklabels=labels,
# yticklabels=labels)
# plt.show()









# Draw a scatter plot while assigning point colors and sizes to different
# variables in the dataset


# f, ax = plt.subplots(figsize=(6.5, 6.5))
# sns.despine(f, left=True, bottom=True)
# clarity_ranking = ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]
# sns.scatterplot(x="carat", y="price",
#                 hue="clarity", size="depth",
#                 palette="ch:r=-.2,d=.3_r",
#                 hue_order=clarity_ranking,
#                 sizes=(1, 8), linewidth=0,
#                 data=diamonds, ax=ax)


#sns.heatmap(reader[["Rented Bike Count","Temperature(∞C)","Wind speed (m/s)","Hour","Visibility (10m)","Dew point temperature(∞C)","Solar Radiation (MJ/m2)","Seasons","Holiday","Functioning Day"]].corr(),annot=True, cmap='Reds')






#pd.read_csv('C:\Users\User\Downloads\SeoulBikeData')

#url='C:\Users\User\Downloads\SeoulBikeData'


#df = pd.read_excel(url)
#df

