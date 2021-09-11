import numpy as np

arr=[]
N, M = map(int,input().split())
for i in range(N):
    my_arr=list(map(int,input().split()))
    arr.append(my_arr)
arr=np.array(arr)
c=np.min(arr, axis = 1) 
print(np.max(c))

