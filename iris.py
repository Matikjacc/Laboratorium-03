import pandas as pd
import matplotlib.pyplot as plt

pl = pd.read_csv('iris.csv')

setosa = pl[pl['class'] == 'Iris-setosa']
versicolor = pl[pl['class'] == 'Iris-versicolor']
virginica = pl[pl['class'] == 'Iris-virginica']


sepallength_sepalwidth_plot = setosa.plot.scatter(x = 'sepallength',y = 'sepalwidth', c = 'red', label = 'setosa')
versicolor.plot.scatter(x = 'sepallength',y = 'sepalwidth', c = 'blue',label = 'versicolor', ax = sepallength_sepalwidth_plot)
virginica.plot.scatter(x = 'sepallength',y = 'sepalwidth', c = 'green',label = 'virginica',ax = sepallength_sepalwidth_plot)
plt.show()
sepallength_petallength_plot = setosa.plot.scatter(x = 'sepallength',y = 'petallength', c = 'red', label = 'setosa')
versicolor.plot.scatter(x = 'sepallength',y = 'petallength', c = 'blue',label = 'versicolor',ax = sepallength_petallength_plot)
virginica.plot.scatter(x = 'sepallength',y = 'petallength', c = 'green',label = 'virginica',ax = sepallength_petallength_plot)
plt.show()
sepallength_petalwidth_plot = setosa.plot.scatter(x = 'sepallength',y = 'petalwidth', c = 'red', label = 'setosa')
versicolor.plot.scatter(x = 'sepallength',y = 'petalwidth', c = 'blue',label = 'versicolor',ax = sepallength_petalwidth_plot)
virginica.plot.scatter(x = 'sepallength',y = 'petalwidth', c = 'green',label = 'virginica',ax = sepallength_petalwidth_plot)
plt.show()
sepalwidth_petallength_plot = setosa.plot.scatter(x = 'sepalwidth',y = 'petallength', c = 'red', label = 'setosa')
versicolor.plot.scatter(x = 'sepalwidth',y = 'petallength', c = 'blue',label = 'versicolor',ax = sepalwidth_petallength_plot)
virginica.plot.scatter(x = 'sepalwidth',y = 'petallength', c = 'green',label = 'virginica',ax = sepalwidth_petallength_plot)
plt.show()
sepalwidth_petalwidth_plot = setosa.plot.scatter(x = 'sepalwidth',y = 'petalwidth', c = 'red', label = 'setosa')
versicolor.plot.scatter(x = 'sepalwidth',y = 'petalwidth', c = 'blue',label = 'versicolor',ax = sepalwidth_petalwidth_plot)
virginica.plot.scatter(x = 'sepalwidth',y = 'petalwidth', c = 'green',label = 'virginica',ax = sepalwidth_petalwidth_plot)
plt.show()
petallength_petalwidth_plot = setosa.plot.scatter(x = 'petallength',y = 'petalwidth', c = 'red', label = 'setosa')
versicolor.plot.scatter(x = 'petallength',y = 'petalwidth', c = 'blue',label = 'versicolor',ax = petallength_petalwidth_plot)
virginica.plot.scatter(x = 'petallength',y = 'petalwidth', c = 'green',label = 'virginica',ax = petallength_petalwidth_plot)
plt.show()
