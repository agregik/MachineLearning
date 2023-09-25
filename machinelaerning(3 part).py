# Глава 3 Упорядочение данных

# import pandas as pd

# url = 'https:// tinyurl.com/titanic-csv'

# Загрузить данные как фрейм данных
# dataframe = pd.read_csv(url)

# Взглянуть на первые пять строк
# print(dataframe(5))

# 3.1 Создание фрейма данных и 3.2 Описание данных

import pandas as pd

# Создать фрейм данных DataFrame
dataframe = pd.DataFrame()

# Добавить столбцы
dataframe['Имя'] = ['Никита Боков', 'Рома Алиев']
dataframe['Возраст'] = [18, 17]
dataframe['Водитель'] = [True, False]
dataframe['Гендер'] = ['Мужчина', 'Мужчина']
# Создать строку и добавить её в конец фрейма данных
dataframe.loc[len(dataframe.index)] = ['Анна Буланникова', 17, True, 'Девушка']
dataframe.loc[len(dataframe.index)] = ['Гриша Боков', 13, False, 'Мужчина']

# Взглянуть на фрейм данных
# print(dataframe)

# НАЧАЛО 3.2 ПУНКТА

# Взглянуть на первую строку фрейма данных
# print(dataframe.iloc[0])

# Взглянуть на первые две строки
# print(dataframe.head(2))

# Взглянуть на размерность матрицы
# print(dataframe.shape)

# Взглянуть на статистику
# print(dataframe.describe())

# 3.2 Навигация по фреймам данных

# Выбрать три строки
# print(dataframe.iloc[1:4])

# Выбрать четыре строки
# print(dataframe.iloc[:4])

# Задать индекс для поиска значений чего-либо (Имя)
# dataframe = dataframe.set_index(dataframe['Имя'])

# Показать строку с нужным значением
# print(dataframe.loc['Анна Буланникова'])

# 3.4 Выбор строк на основе условных конструкций

# Показать верхние две строки, где столбец 'Возраст' равняется 17
# print(dataframe[dataframe['Возраст'] == 17].head(2))

# Отфильтровать строки по нужным значениям
# print(dataframe[(dataframe['Возраст'] == 18) & (dataframe['Водитель'] == True)])

# 3.5 Замена значений

# Заменить значения, показать две строки (1)
# print((dataframe['Имя'].replace('Никита Боков', 'Nikita Bokov').head(2)))

# Заменить значения, показать две строки (2)
# print(dataframe.replace(True, 'Yes'))

# Заменить значения, показать две строки (3)
# print(dataframe.replace(r'lst', 'First', regex=True).head(2))

# 3.6 Переименовывание столбцов

# Переименовать столбец и показать его изменения
# print(dataframe.rename(columns={'Возраст': 'Age'}))

# Переименовать несколько столбцов и показать его изменения
# print(dataframe.rename(columns={'Водитель': 'Driver', 'Имя': 'Name'}))

# Загрузить библиотеку collections

import collections

# Создать словарь
column_names = collections.defaultdict(str)

# Создать ключи
# for name in dataframe.columns:
# column_names[name]
# print(column_names)

# 3.7 Нахождение минимума, максимума, суммы, среднего арифметического и количества

# Вычислить статистические показатели
# print('Максимум:', dataframe['Возраст'].max())
# print('Минимум:', dataframe['Возраст'].min())
# print('Cреднее:', dataframe['Возраст'].std())
# print('Сумма:', dataframe['Возраст'].sum())
# print('Количество:', dataframe['Возраст'].count())

# Показать количества значений
# print(dataframe.count())

# 3.8 Нахождение уникальных значений

# Выбрать уникальные значения
# print(dataframe['Имя'].unique())

# Показать количества появлений
# print(dataframe['Возраст'].value_counts())

# Показать количество уникальных значений по нужному параметру
# print(dataframe['Возраст'].nunique())

# 3.9 Отбор недостающих значений

# Выбрать пропущенные значения и показать их
# print(dataframe[dataframe['Возраст'].isnull()])

# Попытаться заменить пропущенные значения с NaN (Заранее не выйдет, т.к нужно импортировать библиотеку)
# dataframe['Гендер'] = dataframe['Гендер'].replace['Мужчина', Nan]
# print(dataframe)


import pandas as np

# Заменить значения с NaN
dataframe['Гендер'] = dataframe['Гендер'].replace('Мужчина', np.NaT)
# print(dataframe)

# 3.10 Удаление столбцов

# Удалить столбец по заданному параметру
dataframe = dataframe.drop('Возраст', axis=1)
# print(dataframe)

# Отбросить столбцы по заданному параметру
dataframe = dataframe.drop(['Имя', 'Возраст'], axis=1)
# print(dataframe.head(2))
