import numpy as np

# Создать вектор как строку
vector_row = np.array([1, 2, 3])
# Создать вектор как столбец
vector_column = np.array([[1],
                          [2],
                          [3]])

# Создать матрицу
matrix = np.array([[1, 2],
                   [1, 2],
                   [1, 2]])

matrix_object = np.mat([[1, 2],
                        [1, 2],
                        [1, 2]])

# Загрузить библиотеку
from scipy import sparse

# Создать матрицу
matrix2 = np.array([[0, 0],
                    [0, 1],
                    [3, 0]])
# Создать разреженную матрицу - строку (CSR - матрицу)

matrix_sparse = sparse.csr_matrix(matrix2)
# print(matrix_sparse)

# Создать более крупную разреженную матрицу - строку, но сначала создадим обычную матрицу

matrix_larger = ([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 0, 0, 0, 0, 0, 0, 0],
                  [3, 0, 0, 0, 0, 0, 0, 0, 0]])

matrix_larger_sparse = sparse.csr_matrix(matrix_larger)
# Взглянуть на исходную разреженную матрицу
# print(matrix_sparse)

# Взглянуть на более крупную разреженную матрицу
# print(matrix_larger_sparse)


# 1.4 ВЫБОР ЭЛЕМЕНТОВ

import numpy as np

# Создать вектор - строку
vector = np.array([1, 2, 3, 4, 5, 6])

# Создать матрицу
matrix4 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
# Выбрать 3 элемент в векторе
# print(vector[2])

# Выбрать вторую строку второй элемент в матрице
# print(matrix4[1, 1])


# 1.5 Описание матрицы

import numpy as np

# Создать матрицу
matrix5 = np.array([[1, 2, 3, 4],
                    [5, 6, 7, 8],
                    [9, 10, 11, 12]])

# Взглянуть на кол - во строк и столбцов
# print(matrix5.shape)

# Взглянуть на кол - во элементов (строки * столбцы)
# print(matrix5.size)

# Взглянуть на кол - во размерностей
# print(matrix5.ndim)


# 1.6 Применение операций к елементам

import numpy as np

matrix6 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

# Make function that add 100 to smth
add_100 = lambda i: i + 100

# Make vectorized function
vectorized_add_100 = np.vectorize(add_100)

# Add this func to all elements of the matrix
vectorized_add_100(matrix6)
# print(vectorized_add_100(matrix6))

# 1.7 Find max or min in array

import numpy as np

matrix7 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

# print(np.max(matrix7))
# print(np.min(matrix7))

# Find max element in every column (Столбец)
# print(np.max(matrix7, axis=0))

# Find max element in every line (Строка)
# print(np.max(matrix7, axis=1))

# 1.8 Вычисление среднего значения, дисперсии и стандартного отклонения

import numpy as np

matrix8 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

# Вывести среднее значение
# print(np.mean(matrix8))

# Вернуть дисперсию
# print(np.var(matrix8))

# Вернуть стандартное отклонение
# print(np.std(matrix8))

# Найти среднее значение в каждом отдельном столбце
# print(np.mean(matrix8, axis=0))

# Реформирование массивов

import numpy as np

matrix9 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9],
                    [10, 11, 12]])

# Реформировать таблицу в матрицу 2 * 6
# print(matrix9.reshape(2, 6))

# Увидеть размер матрицы
# print(matrix9.size)

# Увидеть одну строку и столько столбцов, сколько необходимо
# print(matrix9.reshape(1, -1))

# Увдить одномерный массив этой длины
# print(matrix9.reshape(12))


