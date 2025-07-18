import numpy as n
arr1=n.array([1,2,3,4])
print(arr1)

arr2=n.array([[1,2],[3,4]])
print(arr2)

arr3=n.array([10,20,30,40])
print(arr3)

zeros=n.zeros((2,3))
print(zeros)

ones=n.ones((2,3))
print(ones)

range_arr=n.arange(0,10,2)
print(range_arr)

result_add=arr1 + 5
print(result_add)

result_mul=arr1*2
print(result_mul)

result_elem_add=arr1+arr3
print(result_elem_add)

result_elem_mul = arr1*arr3
print(result_elem_mul)

arr1_reshaped=arr1.reshape((2,2))
print(arr1_reshaped)

arr2_flattened= arr2.flatten()
print(arr2_flattened)

sum_all=arr1.sum()
print(sum_all)

mean_val=arr2.mean()
print(mean_val)

max_val=arr2.max()
print(max_val)

min_val=arr2.min()
print(min_val)

sum_columns=arr2.sum(axis=0)
print(sum_columns) 

sum_rows=arr2.sum(axis=1)
print(sum_rows)
