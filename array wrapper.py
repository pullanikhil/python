import numpy as np
import array
class array1(array.array):
    arraym1 = np.array((1,6,7,8))
    arraym2 = np.array([2,3,4,5])
    def array_addition(self):
        resultarray = self.arraym1+self.arraym2
        print("the array_addition function returns the result array")
        return resultarray
arrayobj =array1('f')
#arrayobj.arraym1 = np.array([[1,2,3,4],[12,24,36,48]])
#arrayobj.arraym2 = np.array([[2.5,4,6,8],[12,12,24,36]])
#resultarray = arrayobj.array_addition()
#print("array after addition:\n",resultarray)
print(arrayobj.array_addition())
