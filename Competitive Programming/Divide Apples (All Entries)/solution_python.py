n = int(input())
apples = list(map(int,input().split()))
final_count = sum(apples)//n

difference = [i-final_count for i in apples]

com = [difference[0]]

for i in difference[1:]:
    com.append(i+com[-1])  # last element is com[-1]

com.sort()

mid = com[len(com)//2]

com = [abs(i-mid) for i in com]

print(sum(com))
