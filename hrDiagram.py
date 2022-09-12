import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("https://raw.githubusercontent.com/adamlamee/CODINGinK12/master/data/stars.csv") #importing star data

plt.scatter(np.log10(data.temp),data.absmag, s = 0.3)

#labeling the plot
plt.title("H-R Diagram")
plt.xlabel("log(T)")
plt.ylabel("Absolute Magnitude")

#fixing the limit
plt.xlim(np.log10(15000),np.log10(2000))
plt.ylim(20,-15)

plt.show()
