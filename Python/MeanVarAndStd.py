import numpy as np

arr=[]
N, M = map(int,input().split())
for i in range(N):
    my_arr=list(map(int,input().split()))
    arr.append(my_arr)
arr=np.array(arr)
print(np.mean(arr, axis = 1))   
print(np.var(arr, axis=0))
a=np.std(arr, axis=None)
print(round(a, 11))
