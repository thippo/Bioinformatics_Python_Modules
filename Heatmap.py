import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def heatmap(df ,cmap=plt.cm.gray_r):
	fig=plt.figure()
	ax=fig.add_subplot(111)
	axim=ax.imshow(df.values,cmap=cmap,interpolation='nearest')
	ax.set_xlabel(df.columns.name)
	ax.set_xticks(np.arange(len(df.columns)))
	ax.set_xticklabels(list(df.columns))
	ax.set_ylabel(df.index.name)
	ax.set_yticks(np.arange(len(df.index)))
	ax.set_yticklabels(list(df.index))
	plt.colorbar(axim)
	plt.show()

a=pd.DataFrame(np.random.randn(9).reshape(3,3),index=['x','y','z'],columns=['a','b','c'])
a.index.name='xy'
a.columns.name='abc'
heatmap(a)