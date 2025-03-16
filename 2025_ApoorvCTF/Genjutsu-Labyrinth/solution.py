from sympy import mod_inverse
from sympy import primerange
import numpy as np

def min_cost_path(matrix):
    rows, cols = len(matrix), len(matrix[0])
    dp = np.zeros((rows, cols), dtype=int)
    path = [["" for _ in range(cols)] for _ in range(rows)]
    
    dp[0][0] = matrix[0][0]
    path[0][0] = "Start "
    
    for j in range(1, cols):
        dp[0][j] = dp[0][j-1] + matrix[0][j]
        path[0][j] = path[0][j-1] + "S "
    
    for i in range(1, rows):
        dp[i][0] = dp[i-1][0] + matrix[i][0]
        path[i][0] = path[i-1][0] + "D "
    
    for i in range(1, rows):
        for j in range(1, cols):
            if dp[i-1][j] < dp[i][j-1]:
                dp[i][j] = dp[i-1][j] + matrix[i][j]
                path[i][j] = path[i-1][j] + "D "
            else:
                dp[i][j] = dp[i][j-1] + matrix[i][j]
                path[i][j] = path[i][j-1] + "R " 
    return path[-1][-1]

def decrypt(encry_grid, mod=101):
    size = len(encry_grid)
    b = int(encry_grid[0][0])  # b — первый элемент в зашифрованной матрице
    possible_a = list(primerange(2, 12))  # Простые числа от 2 до 11
    
    # Найти a
    a = None
    for candidate_a in possible_a:
        possible_n = [(candidate_a * n + b) % mod for n in range(10)]
        if int(encry_grid[0][1]) in possible_n:
            a = candidate_a
            break
    
    if a is None:
        raise ValueError("Не удалось найти подходящее a")
    
    a_inv = mod_inverse(a, mod)
    
    # Дешифруем
    decrypted_grid = []
    for row in encry_grid:
        decrypted_row = [(a_inv * (int(enc_val) - b)) % mod for enc_val in row]
        decrypted_grid.append(decrypted_row)
    
    return decrypted_grid

response = ['00 21 03 12 09 06 09 18 24 27',
'27 21 24 03 12 00 21 24 15 21',
'24 12 09 15 18 03 27 15 12 27',
'15 27 24 09 18 21 21 12 18 03',
'24 15 24 18 06 18 09 21 00 18',
'21 24 24 06 24 03 15 15 12 15',
'00 18 12 15 27 24 24 24 09 06',
'09 27 12 15 03 24 27 27 06 15',
'03 09 27 03 21 09 03 24 06 12',
'00 21 00 24 27 15 12 12 12 00']

encry_grid = []

for i in range(10):
    encry_grid.append( str(response[i]).split(' ') )

precrypted_grid = decrypt(encry_grid)
for i in precrypted_grid:
    print(i)

solution = min_cost_path(precrypted_grid)

print(solution, solution.count('D'), solution.count('R'))
