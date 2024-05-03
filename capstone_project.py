import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\MICHEAL\OneDrive\Documents\usa_county_wise.csv")
#print(data.head(5))
#print(data.columns)
#print(data.describe)
#print(data.columns)
#print(data.isnull().sum())

#print(data.columns)
sns.set_style("whitegrid")

#Relating the variables with scatterplots
plt.figure(figsize=(8,10))
sns.relplot(x="Confirmed", y="Deaths", data=data, alpha=0.7, color='green')
plt.title("Relationship between Confirmed Cases and Deaths")
plt.xlabel("Confirmed Cases")
plt.ylabel("Deaths")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()