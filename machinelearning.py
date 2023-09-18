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
# Вывести разреженную матрицу
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

# 1.10 Транспортирование вектора в матрицу

import numpy as np

matrix10 = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])
# Транспонировать матрицу
# print(matrix10.T)

# 1.11 Сглаживание матрицы

import numpy as np

matrix11 = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

# Сгладить матрицу (привести к одномерному массиву)
# print(matrix11.flatten())

# 1.12 Нахождение ранга матрицы

import numpy as np

matrix12 = np.array([[1, 1, 1],
                     [1, 1, 10],
                     [1, 1, 15]])

# Вернуть ранг матрицы
# print(np.linalg.matrix_rank(matrix12))

# 1.13 Вычисление определителя матрицы

import numpy as np

matrix13 = np.array([[1, 2, 3],
                     [2, 4, 6],
                     [3, 8, 9]])

# Вернуть определитель матрицы
# print(np.linalg.det(matrix13))

# 1.14 Получение диагонали матрицы

import numpy as np

matrix14 = np.array([[1, 2, 3],
                     [2, 4, 6],
                     [3, 8, 9]])

# Вернуть диагональные элементы
# print(matrix14.diagonal())

# Вернуть диагональ на одну выше главной диагонали
# print(matrix14.diagonal(offset=1))

# Вернуть диагональ на одну ниже главной диагонали
# print(matrix14.diagonal(offset=-1))

# 1.15 Вычисление следа матрицы

import numpy as np

matrix15 = np.array([[1, 2, 3],
                     [2, 4, 6],
                     [3, 8, 9]])

# Вернуть след
# print(matrix15.trace())

# Альтернативный способ вычисления следа матрицы вернув сумму её эл-ов
# print(sum(matrix15.diagonal()))

# 1.16 Нахождение собственных значений и собственных векторов

import numpy as np

matrix16 = np.array([[1, -1, 3],
                     [1, 1, 6],
                     [3, 8, 9]])

# Вычислить собственные значения и векторы
eigenvalues, eigenvectors = np.linalg.eig(matrix16)
# print(eigenvalues)
# print(eigenvectors)

# 1.17 Вычисление скалярных произведений

import numpy as np

vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 6])

# Вычислить скалярное произведение
# print(np.dot(vector_a,vector_b))

# Альтернативный способ нахождения скалярного произведения
# print(vector_a @ vector_b)

# 1.18 Сложение и вычитание матриц

import numpy as np

matrix_a = np.array([[1, 1, 1],
                     [1, 1, 1],
                     [1, 1, 2]])

matrix_b = np.array([[1, 3, 1],
                     [1, 3, 1],
                     [1, 3, 8]])

# Сложить матрицы
# print(np.add(matrix_b, matrix_a))
# print(matrix_b + matrix_a)

# Вычесть из одной матрицу другую
# print(matrix_a - matrix_b)
# print(np.subtract(matrix_a, matrix_b))

# Умножить одну матрицу на другую
# print(matrix_a * matrix_b)

# 1.20 Обращение матрицы

import numpy as np

matrix20 = np.array([[1, 4],
                     [2, 5]])

# Вычислить обратную матрицу
# print(np.linalg.inv(matrix20))

# 1.21 Генерирование случайных значений

import numpy as np

# Задать начальное значение для генератора псевдослучайных чисел
np.random.seed(0)

# Сгенерировать три случайных ВЕЩЕСТВЕННЫХ числа между 0 и 1
# print(np.random.random(3))

# Сгенерировать три случайных ЦЕЛЫХ числа между 1 и 10
# print(np.random.randint(0, 11, 3))

# Извлечь три числа из нормального распределения со средним
# равным 0 и стандартным отклонением равным 1
# print(np.random.normal(0.0, 1.0, 3))

# Извлечь три числа из логистического распределения со средним
# равным 0 и масштабом равным 1
# print(np.random.logistic(0, 1, 3))

# Извлечь три числа, которые больше или равны 1 и меньше 2
# print(np.random.uniform(1, 2, 3))


