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
dataframe['Гендер'] = dataframe['Мужчина', 'Мужчина']
# Создать строку и добавить её в конец фрейма данных
dataframe.loc[len(dataframe.index)] = ['Анна Буланникова', 17, True, 'Девушка']
dataframe.loc[len(dataframe.index)] = ['Гриша Боков', 13, False, 'Мужчина']
# dataframe.loc[len(dataframe.index)] = ['Гриша Боков', 13, False, 'Мужчина']
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

# import pandas as np

# Заменить значения с NaN
# dataframe['Гендер'] = dataframe['Гендер'].replace('Мужчина', np.NaT)
# print(dataframe)

# 3.10 Удаление столбцов

# Удалить столбец по заданному параметру
# dataframe = dataframe.drop('Возраст', axis=1)
# print(dataframe)

# Отбросить столбцы по заданному параметру
# dataframe = dataframe.drop(['Имя', 'Возраст'], axis=1)
# print(dataframe)

# Отбросить стобец по индексу (можно использовать такой метод,если неизвестно название столбца)
dataframe_drop_column = dataframe.drop(dataframe.columns[1], axis=1)
# print(dataframe_drop_column)

# Создать новую переменную, для того чтобы не менять основной фрейм данных и рассмотреть его изменения в отдельной переменной
dataframe_name_dropped = dataframe.drop(dataframe.columns[0], axis=1)
# print(dataframe_name_dropped)

# 3.11 Удаление строки

# Удалить строки по заданному параметру
dataframe_drop_stroku = dataframe[dataframe['Гендер'] != 'Мужчина']
# print(dataframe_drop_stroku)

# Удалить строку по уникальному значению
dataframe_drop_poimeni = dataframe[dataframe['Имя'] != 'Гриша Боков']
# print(dataframe_drop_poimeni)

# Удалить строку по индексу
dataframe_drop_poindeksu = dataframe[dataframe.index != 0]
# print(dataframe_drop_poindeksu)


# 3.12 Удаление повторяющихся строк

# Удалить дубликаты
dataframe_dublicates = dataframe.drop_duplicates()
# print(dataframe_dublicates)

# Показать количество строк в исходном фрейме данных
# print('Количество строк в исходном фрейме данных:', len(dataframe))

# Показать количество строк после дубликации
# print('Количество строк в после дубликации:', len(dataframe.drop_duplicates()))

# Удалить дубликаты (Метод показывает первое появление уникального элемента, а остальные отбрасывает)
# print(dataframe.drop_duplicates(subset=['Гендер']))

# Удалить дубликаты применив метод, позволяющий выбирать по какому критерию будет отбрасывать
# print(dataframe.drop_duplicates(subset=['Возраст'], keep='last'))

# Посмотреть на каких позициях по счёту нах-ся в фрейме данных
# print(dataframe.duplicated())

# 3.13 Группирование строк по значениям (Смотри Notion,у тебя мало данных)

# Сгруппировать строки по значениям столбца 'Возраст', вычислить среднее каждой группы
# print(dataframe.groupby('Возраст').mean())

# Сгруппировать строки, подсчитать строки
# print(dataframe.groupby('Водитель')['Имя'].count())

# Сгруппировать строки, вычислить среднее
# print(dataframe.groupby(['Имя', 'Водитель'])['Возраст'].mean())

# 3.14 Группирование строк по значениям времени

import pandas as pd
import numpy as np

# Создать диапазон дат
time_index = pd.date_range('06/06/2017', periods=100000, freq='30S')

# Создать фрейм данных
dataframe1 = pd.DataFrame(index=time_index)

# Создать столбец случайных значений со значением суммы продаж
dataframe1['Sale_Amount'] = np.random.randint(1, 10, 100000)


# Сгруппировать строки по неделе, вычислить сумму за неделю
# print(dataframe1.resample('W').sum())

# Сгруппировать строки по двум неделям, вычилсить сумму за эти две недели
# print(dataframe1.resample('2W').mean())

# Сгруппировать по месяцу, посчитать строки
# print(dataframe1.resample('M').count())

# Сгруппировать по месяцу с помощью метода label, подсчитать строки
# print(dataframe1.resample('M',label='left').count())

# 3.15 Обход столба в цикле

# Напечатать первые два имени в верхнем регистре
# for name in dataframe['Имя'][0:2]:
# print(name.upper())

# Альтернативный способ вывода двух имен в верхнем регистре
# print([name.upper() for name in dataframe['Имя'][0:2]])

# 3.16 Применение функции ко всем эл-ам в столбце

# Создать функцию

def appercase(x):
    return x.upper()


# Применить функцию, показать две строки
# print(dataframe['Имя'].apply(appercase)[0:2])


# 3.17 Применение функций к группам (Считает кол-во гендеров и выводит их кол-во)
# print(dataframe.groupby('Гендер').apply(lambda x: x.count()))

# 3.18 Конкатенация фреймов данных

import pandas as pd

# Создать фреймы данных
data_a = {'id': ['1', '2', '3'],
          'first': ['Женя', 'Ира', 'Гриша'],
          'last': ['Паша', 'Вера', 'Полина']}
dataframe_a = pd.DataFrame(data_a, columns=['id', 'first', 'last'])

data_b = {'id': ['4', '5', '6'],
          'first': ['Никита', 'Аня', 'Эльдар'],
          'last': ['Костя', 'Рома', 'Саша']}
dataframe_b = pd.DataFrame(data_b, columns=['id', 'first', 'last'])

# Объеденить фреймы данных по строкам (Конкатенировать)
# print(pd.concat([dataframe_a, dataframe_b], axis=0))

# Объеденить фреймы данных по столбцам (Конкатенировать)
# print(pd.concat([dataframe_a, dataframe_b], axis=1))

# Создать строку и добавить её в конец фрейма данных
dataframe_a.loc[len(dataframe_a.index)] = [7, 'Вадим', 'Сергей']

# 3.19 Слияние фреймов данных

# Создать фрейм данных с данными людей
import pandas as pd

employee_data = {'employee_id': ['1', '2', '3', '4'],
                 'name': ['Nikita', 'Anna', 'Roma', 'Kostya']}

dataframe_employees = pd.DataFrame(employee_data, columns=['employee_id', 'name'])

# Создать фрейм данных с данными о продажах людей

sales_data = {'employee_id': ['3', '4', '5', '6'],
              'total sales': [23456, 2512, 7890, 1455]}
dataframe_sales = pd.DataFrame(sales_data, columns=['employee_id', 'total sales'])
# print(dataframe_sales)

# Выполнить слияние фреймов данных (Посмотрит 'employee_id' и вернет значения и сделает их одним целым фреймом)
# print(pd.merge(dataframe_employees, dataframe_sales, on='employee_id'))

# Выполнить внешнее слияние фреймов данных (Сделает единым оба фрейма данных)
# print(pd.merge(dataframe_employees, dataframe_sales, on='employee_id', how='outer'))

# LeetCode (astype), функция позволяющая менять тип данных
# print(df.astype({'numbers':int})))

# LeetCode (fillna), функция позволяющая заполнять нулевые значения
# print(df['quantity'].fillna(0,inplace=True)

# LeetCode (melt), функция позволяющая изменить форму данных в виде таблицы
# pd.melt(df, id_vars=['product'], var_name='quarter', value_name='sales')




