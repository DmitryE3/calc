"""В примере кода разработайте реализацию функции sumUpDiagonals() на JavaScript таким образом, чтобы она возвращала
суммы основной и вторичной диагоналей квадратной матрицы. (Переделано для работы на питон)
"""


def sumUpDiagonals(size_matrix, matrixExample):
    summ_diag = 0
    sum_second_diag = 0
    for i in range(size_matrix):
        summ_diag += matrixExample[i][i]
        sum_second_diag += matrixExample[i][size_matrix - 1 - i]
    return summ_diag, sum_second_diag


matrixExample = [[1, 2, 3, 4], [4, 5, 6, 5], [7, 8, 9, 7], [7, 8, 9, 7]]
print(sumUpDiagonals(4, matrixExample))
