# Глава 3 Упорядочение данных

# import pandas as pd

# url = 'https:// tinyurl.com/titanic-csv'

# Загрузить данные как фрейм данных
# dataframe = pd.read_csv(url)

# Взглянуть на первые пять строк
# print(dataframe(5))

# 3.1 Создание фрейма данных

import pandas as pd

# Создать фрейм данных DataFrame
dataframe = pd.DataFrame()

# Добавить столбцы
dataframe['Имя'] = ['Никита Боков', 'Стивен Стивенсон']
dataframe['Возраст'] = [18, 17]
dataframe['Водитель'] = [True, False]

# Создать строку и добавить её в конец фрейма данных
dataframe.loc[len(dataframe.index)] = ['Анна Буланникова', 17, True]
print(dataframe)
