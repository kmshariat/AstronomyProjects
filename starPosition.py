import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("https://raw.githubusercontent.com/adamlamee/CODINGinK12/master/data/stars.csv") #importing star data

fig = plt.figure(figsize=(15, 4))
plt.scatter(data.ra, data.dec, s = 0.2)

#labeling the plot
plt.title("Stars in our sky")
plt.xlabel("RA")
plt.ylabel("Dec")

#fixing the limits
plt.xlim(0,24)
plt.ylim(-90,90)

plt.show()
