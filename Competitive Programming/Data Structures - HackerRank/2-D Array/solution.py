bigArray = []
sums = []
for _ in range(6):
    row = list(map(int,input().split()))
    bigArray.append(row)
for i in range(len(bigArray)-2):
    for j in range(len(bigArray[i])-2):
        hourSum = []
        hourSum.append(bigArray[i][j])
        hourSum.append(bigArray[i][j+1])
        hourSum.append(bigArray[i][j+2])
        hourSum.append(bigArray[i+1][j+1])
        hourSum.append(bigArray[i+2][j])
        hourSum.append(bigArray[i+2][j+1])
        hourSum.append(bigArray[i+2][j+2])
        sums.append(sum(hourSum))
#print(sums)
print(max(sums))
        
        
        
