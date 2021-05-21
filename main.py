#Ferramentas Numpy
#Analise de dados Iris DataSet
#link banco de dados: https://archive.ics.uci.edu/ml/datasets/Iris
#attributed information
#1. sepal length in cm
#2. sepal width in cm
#3. petal length in cm
#4. petal width in cm
#5. class:
#-- Iris Setosa
#-- Iris Versicolour
#-- Iris Virginica

import numpy as np

import matplotlib.pyplot as plt


#acessando somente os valores caracteristicos sem se importar com a classe
data = np.genfromtxt('iris.data', delimiter=',', usecols =(0,1,2,3))
quantidadeDados = len(data)
print(quantidadeDados)

#grafico comprimento sepalas Iris Setosa
plt.figure(1)
sepalLengthSetosa = data[:50,0]
plt.plot(sepalLengthSetosa, c='Red', ls=':', marker='s', ms=8)
plt.title('comprimento sepalas Iris Setosa')
#plt.show()

#grafico comprimento sepalas Iris Versicolour
plt.figure(2)
sepalLengthVersicolour = data[50:100,0]
plt.plot(sepalLengthVersicolour, c='Blue', ls=':', marker='s', ms=8)
plt.title('comprimento sepalas Iris Versicolour')
#plt.show()

#grafico comprimento sepalas Iris Virginica
plt.figure(3)
sepalLengthVirginica = data[100:150,0]
plt.plot(sepalLengthVirginica, c='Green', ls=':', marker='s', ms=8)
plt.title('comprimento sepalas Iris Virginica')
#plt.show()
plt.figure(4)

#comparação comprimentos
plt.plot(sepalLengthSetosa, c='Red', ls=':', marker='s', ms=8, label ='Setosa')
plt.plot(sepalLengthVersicolour, c='Blue', ls=':', marker='s', ms=8, label ='Versicolour')
plt.plot(sepalLengthVirginica, c='Green', ls=':', marker='s', ms=8, label ='Virginica')
plt.title('Comparação comprimento sepalas')
plt.legend
#plt.show()

#medias dos comprimentos
meanLengthSetosa = sepalLengthSetosa.mean()
meanLengthVersicolour = sepalLengthVersicolour.mean()
meanLengthVirginica = sepalLengthVirginica.mean()
