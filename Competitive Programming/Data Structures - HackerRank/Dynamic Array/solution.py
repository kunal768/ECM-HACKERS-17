
n,Q = map(int,input().split())
lis = [[] for i in range(n)]
lastAnswer = 0
for _ in range(Q):
    q,x,y = map(int,input().split())
    index =(x^lastAnswer)%n
    arr = lis[index]
    #print(query)
    if q is 1:
        arr.append(y)
        #print(lis)
    elif q is 2:
        size = len(arr)
        lastAnswer = arr[y%size]
        print(lastAnswer)
    else:
        raise ValueError()
    
