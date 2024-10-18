# Author: Seda Tarverdyan | Copyright (c) 2024 | Use of this code requires keeping this copyright notice.
import numpy as np


matrix = np.array([[1, 0, 1, 0],
                   [1, 1, 1, 0],  
                   [1, 1, 0, 0],
                   [0, 0, 1, 0]])  

# տողի զույգություն
def check_row_parity(row):
    return row.sum() % 2 == 0

# սյան զույգություն
def check_column_parity(matrix, col_idx):
    return matrix[:3, col_idx].sum() % 2 == 0
 
wrong_rows = []
for i in range(4):  
    if not check_row_parity(matrix[i, :4]):
        wrong_rows.append(i)


wrong_cols = []
for j in range(4):  
    if not check_column_parity(matrix, j):
        wrong_cols.append(j)


if not wrong_rows and not wrong_cols:
    print("Մատրիցում սխալ չկա։")
elif len(wrong_rows) == 1 and len(wrong_cols) == 1:
    print(f"Սխալը գտնվում է ({wrong_rows[0]}, {wrong_cols[0]}) ինդեքսում։")
    
    #ուղղում
    matrix[wrong_rows[0], wrong_cols[0]] = 1 if matrix[wrong_rows[0], wrong_cols[0]] == 0 else 0

    
    print("Ուղղված մատրիցը:")
    print(matrix)
elif len(wrong_rows) > 1 or len(wrong_cols) > 1:
    print("Մատրիցում երկու սխալ կա")
