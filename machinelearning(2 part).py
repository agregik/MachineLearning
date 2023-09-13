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
# Взглянуть на матрицу признаков и вектор целей
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

# Взглянуть на матрицу признаков и вектор целей
print('Матрица признаков\n', features3[:3])
print('Вектор целей\n', target3[:3])

# Создать набор данных, который хорошо функционирует с кластеризующими методами
# библиотека для создания предлагает метод создания скоплений точек

from sklearn.datasets import make_blobs

# Сгенерировать матрицу
