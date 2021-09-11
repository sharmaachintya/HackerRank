import numpy as np

arr1=[]
arr2=[]
while True:
    my_arr1=list(map(int,input().split()))
    arr1.append(my_arr1)
    break
arr1=np.array(arr1)
while True:
    my_arr2=list(map(int,input().split()))
    arr2.append(my_arr2)
    break
arr2=np.array(arr2)
print(int(np.inner(arr1, arr2)))
print(np.outer(arr1, arr2))




