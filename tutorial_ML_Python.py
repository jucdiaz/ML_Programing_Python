# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 14:36:24 2017

@author: jucadiaz
"""

from sklearn import datasets

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

## De la manera anterior son cargadas las librerias a importar

plt.style.use('ggplot')


iris = datasets.load_iris() # Carga el conjunto de datos de prueba

type(iris)

print(iris.keys())

type(iris.data), type(iris.target) # nos dice el typo de datos que es el de la columna data y target

iris.data.shape # seleciona el valor dentro de data llamadao shape

iris.target_names  


X = iris.data
y = iris.target
df = pd.DataFrame(X, columns=iris.feature_names) # de la libreria pandas llama la funcion DataFrame 
# y convierte la los datos X en datafrmae y se le colocan los nombres de las columnas dado por feature_names
#

print(df.head()) # con el print imprime sin el out

df.info() # describe la caracteristica de los datos que columnas son los datos y todo eso

df.describe() # Realizar estadisticas basicas como un summary() en R por columnas.


pd.scatter_matrix(df, c = y, figsize = [8, 8], s=150, marker = 'D') 
# realiza una matriz de dispersion grafica clasificada por la y en el centro realiza histogramas

## Otros graficos adicionales


import seaborn as sns
sns.set(style="darkgrid")
titanic = sns.load_dataset("titanic")
ax = sns.countplot(x="class", data=titanic)

import seaborn as sns
sns.set_style("whitegrid")
tips = sns.load_dataset("tips")
ax = sns.barplot(x="day", y="total_bill", data=tips)


########################################
### Como relizar un K-Vecino mas cercado, Metodo Supervisado
########################################

from sklearn.neighbors import KNeighborsClassifier # Importo libro de clasificacion por vecino mas cercano

knn = KNeighborsClassifier(n_neighbors=6) # defino el numero de vecindades de entrada 6

knn.fit(iris['data'], iris['target']) 

iris['data'].shape

iris['target'].shape

X_new = iris.data
prediction = knn.predict(X_new)

X_new.shape

print('Prediction {}'.format(prediction))

### Particionamiento de la base de datos para que sea una parte de entrenamiento,
#otra de validacion o prueba

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test =train_test_split(X, y, test_size=0.3,random_state=21, stratify=y)

knn = KNeighborsClassifier(n_neighbors=8)

knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

print("Test set predictions:\n {}".format(y_pred))

knn.score(X_test, y_test)
















