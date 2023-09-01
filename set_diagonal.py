import numpy as np
square_matrix = np.array([[0,4,0,0],[0,5,0,0],[0,6,0,0],[0,7,0,0]])
print("the given square matrix : \n",square_matrix)
np.fill_diagonal(square_matrix,1)
print("the updated matrix is:\n",square_matrix)

