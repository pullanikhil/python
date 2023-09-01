import numpy as np
twoDarray = np.array([[1,2,],[6,7,]])
imatrix = np.eye(2,dtype=int)
print("the two dimensional array is :\n",twoDarray)
print("the eye matrix is :\n",imatrix)
addition_matrix = twoDarray + imatrix
print("the addition of the matrix is:\n",addition_matrix)
multipication_matrix = twoDarray * imatrix
print("the multiplication of the matrix is :\n",multipication_matrix)

# creats ones matrix
firstarray = np.ones((2,2),dtype=int)
print("the ones array is :\n",firstarray)
addition_matrix1 = twoDarray + firstarray
print("the addition of the matrix is :\n",addition_matrix1)
multipication_matrix1 = twoDarray * firstarray
print("the multiplication of the matrix is :\n",multipication_matrix1)

print("the ones array is :\n",firstarray)
addition_matrix2 = imatrix + firstarray
multipication_matrix2 = imatrix * firstarray
print("the addition of the i matrix is :\n",addition_matrix2)
print("the multiplication of the i matrix is :\n",multipication_matrix2)

myarray = np.array([[1,3,4,5],[7,3,4,2],[3,2,6,8]])
unique_value,counts=np.unique(myarray,return_counts=True)
unique_value=unique_value[counts==1]
print(unique_value)


