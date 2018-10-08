
t = int(input())
for _ in range(t):
  emptyLine = input()
  s = list(input().split(" "))
  beforeEqual = []
  afterEqual = []
  for i in s :
    if "machula" in i :
      pos = s.index(i)
    try:
      i = int(i)
      if s.index(str(i)) > s.index("=") :
        afterEqual.append(i)
      elif s.index(str(i)) < s.index("="):
          beforeEqual.append(i)
    except ValueError:
        pass 
  #print(afterEqual , beforeEqual)
  if len(afterEqual) is 0 :
    inkBlot = sum(beforeEqual)
    s[pos] = inkBlot
  else:
    inkBlot = afterEqual[0] - beforeEqual[0]
    s[pos] = inkBlot
  print(*s)

