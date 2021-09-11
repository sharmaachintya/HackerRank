import numpy as np

arr1=[]
arr2=[]
N = int(input())
for i in range(N):
    my_arr1=list(map(int,input().split()))
    arr1.append(my_arr1)
arr1=np.array(arr1)
for i in range(N):
    my_arr2=list(map(int,input().split()))
    arr2.append(my_arr2)
arr2=np.array(arr2)
print(np.dot(arr1,arr2))

