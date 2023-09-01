import numpy as np

zerodarray = np.array([5])
onedimensionarray = np.array([6,7,8,9,10])
resultmultitarray = onedimensionarray * zerodarray


print('the zerodimension array is :',zerodarray)
print('the onedimensionarray is: ',onedimensionarray)
print("the multiplication of onedimensionarray & zeroarray : ",resultmultitarray)

onedimensionarray1 = np.array([2,4,6,8])
onedimensionarray2 = np.array([3,6,9,12])
reultsubractionarray = onedimensionarray1 -onedimensionarray2
print('the subraction of onedimensionarray1 & onedimensionarray2:',reultsubractionarray)

twodimension_array = np.array([[4,8],[6,9]])
twodimension_array1 = np.array([[6,12],[8,10]])
resultmodulusarray = twodimension_array /twodimension_array1
print('the division of twodimension_array & twodimension_array1:\n',resultmodulusarray)
# create arrays with all the possibilities and try with all the atributes & data datypes present in it

threedimension_array1 = np.array([[[6,12,18]],[[9,18,27]]])
threedimension_array2 = np.array([[[2,2,4]],[[10,11,22]]])
resultaddarray = threedimension_array1 + threedimension_array2
print('the addition of threedimension_array1 & threedimension_array2:\n',resultaddarray)



print('the addition of threedimension_array1 & threedimension_array2:\n',threedimension_array1.ndim)
print('the addition of threedimension_array1 & threedimension_array2:\n',twodimension_array1.size)
print('the addition of threedimension_array1 & threedimension_array2:\n',threedimension_array1.shape)



# transpose of an array
transposearray = np.array([[2,4,6,8],[3,6,9,12]])
print(transposearray)
t= transposearray.transpose()
print("\n",t)

























