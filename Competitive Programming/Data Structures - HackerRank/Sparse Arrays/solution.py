n = int(input())
strings = []
queries = []

for _ in range(n):
    strings.append(input())
    
q = int(input())

for _ in range(q):
    queries.append(input())

for i in queries:
  if i in strings:
    print(strings.count(i))
  else:
    print(0)
     
