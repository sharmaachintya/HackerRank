if __name__ == '__main__':
    N = int(input())    
    lis=[]
    for i in range(N):
        s=input().strip().split(" ")
        if s[0]=="insert":
            lis.insert(int(s[1]),int(s[2]))
        elif s[0]=="print":
            print(lis)
        elif s[0]=="remove":
            lis.remove(int(s[1]))
        elif s[0]=="append":
            lis.append(int(s[1]))
        elif s[0]=="sort":
            lis.sort()
        elif s[0]=="pop":
            lis.pop()
        else:
            lis.reverse()
        
