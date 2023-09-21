# 2.1 Загрузка образца набора данных

# Загрузить наборы данных scikit-learn

from sklearn import datasets

# Загрузить набор изображений рукописных цифр
digits = datasets.load_iris()

# Создать матрицу признаков
features = digits.data

# Создать вектор цели
target = digits.target

# Взглянуть на первое изображение
# print(features[0])

# 2.2 Создание симулированного набора данных

# Создать набор данных, предназначенный для использования с лин-ой регрессией

from sklearn.datasets import make_regression

# Сгенерировать матрицу признаков, вектор целей и истинные коэф-ты

features2, target2, coefficients = make_regression(n_samples=100,
                                                   n_features=3,
                                                   n_informative=3,
                                                   n_targets=1,
                                                   noise=0,
                                                   coef=True,
                                                   random_state=1)
# Взглянуть на матрицу признаков и вектор целей (Лин-ая регрессия)
# print('Матрица признаков\n', features2[:3])
# print('Вектор целей\n', target2[:3])

# Создать симулированный набор данных для задачи классификации

from sklearn.datasets import make_classification

# Сгенерировать матрицу признаков и вектор целей

features3, target3 = make_classification(n_samples=100,
                                         n_features=3,
                                         n_informative=3,
                                         n_redundant=0,
                                         n_classes=2,
                                         weights=[.25, .75],
                                         random_state=1)

# Взглянуть на матрицу признаков и вектор целей (Классификация)
# print('Матрица признаков\n', features3[:3])
# print('Вектор целей\n', target3[:3])

# Создать набор данных, который хорошо функционирует с кластеризующими методами
# библиотека для создания предлагает метод создания скоплений точек

from sklearn.datasets import make_blobs

# Сгенерировать матрицу признаков и вектор целей

features4, target4 = make_blobs(n_samples=100,
                                n_features=2,
                                centers=3,
                                cluster_std=0.5,
                                shuffle=False,
                                random_state=1)

# Взглянуть на матрицу признаков и вектор целей (Кластеризующие методы)
# print('Матрица признаков\n', features4[:3])
# print('Вектор целей\n', target4[:3])

import matplotlib.pyplot as plt

# Взглянуть на диаграмму расселения
# plt.scatter(features4[:, 0], features4[:, 1], c=target4)
# plt.show()

# 2.3 Загрузка файлов CSV

import pandas as pd

# Создать URL-адрес
url = 'https://tinyurl.com/simulated-data'

# Загрузить набор данных
dataframe = pd.read_csv(url)

# Взглянуть на первые две строки
# print(dataframe.head(2))

# 2.4 Загрузка данных Excel

import pandas as pd

# Создать URL-адрес
url2 = 'https://tinyurl.com/simulated-excel'

# Загрузить данные для считывания файла Excel
dataframe2 = pd.read_excel(url, sheet_name=0, header=1)

# Взглянуть на первые две строки
print(dataframe.head(2))

# 2.5 Загрзука данных JSON

import pandas as pd

# Создать URL-адрес
url3 = 'https://tinyurl.com/simulated-json'

# Загрузить данные из JSON файла
dataframe3 = pd.read_json(url, orient='columns')

# Взглянуть на первые две строки
print(dataframe3.head(2))

# 2.6 Опрашивание базы данных SQL

import pandas as pd
from sqlalchemy import create_engine

# Создать подключение к базе данных
database_connection = create_engine('sqlite:///sample.db')

# Загрузить данные
dataframe4 = pd.read_sql_query('SELECT * FROM data', database_connection)

# Взглянуть на первые две строки
print(dataframe4.head(2))
