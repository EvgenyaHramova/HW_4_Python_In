# Напишите функцию для транспонирования матрицы 
# Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]

def trans_matrix(matrix_nums, new_matrix_nums):
    for i in range(len(matrix_nums)):
        for j in range(len(matrix_nums[0])):
            new_matrix_nums[j][i] = matrix_nums[i][j]
    return new_matrix_nums

matrix_nums = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
new_matrix_nums = [[0,0,0], [0,0,0], [0,0,0], [0,0,0]]
#new_matrix_nums = [[len(matrix_nums)][len(matrix_nums[0])]]   ???? как записать через длину из первой матрицы???????
print(trans_matrix(matrix_nums, new_matrix_nums))

# print(len(matrix_nums[0]))
# print(len(matrix_nums))

# for i in range(len(matrix_nums)):
#     for j in range(len(matrix_nums[0])):
#         new_matrix_nums[j][i] = matrix_nums[i][j]
# print(new_matrix_nums)

# new_matrix_nums = [[matrix_nums[j][i]  for j in range(len(matrix_nums))] for i in range(len(matrix_nums[0]))]
# print(new_matrix_nums)