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

# Создать строку и добавить её в конец фрейма данных
dataframe.loc[len(dataframe.index)] = ['Анна Буланникова', 17, True]
dataframe.loc[len(dataframe.index)] = ['Гриша Боков', 13, False]
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
print(dataframe.describe())



