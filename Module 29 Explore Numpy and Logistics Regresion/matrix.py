import numpy as np
one_d = np.array([1,2,3,4,5,6])
two_d = np.array([[1,2], [3,4], [5,6]])

# print(one_d)
# print(two_d.ndim)
#dimension
#print(two_d.ndim)
#number_of_items
#print(two_d.size)
#print(two_d.shape)

#data types
print(one_d.dtype)
print(one_d)

diff_type = one_d.astype('f')
print(diff_type.dtype)
print(diff_type)