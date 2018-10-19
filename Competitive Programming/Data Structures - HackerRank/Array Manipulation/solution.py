n , q = map(int,input().split())
lis = [0 for _ in range(n%(10**7))]
for _ in range(q%(10**5)):
    a,b,k = map(int,input().split())
    for i in range(a-1,b):
        lis[i]+=k%(10**9)
print(max(lis))
