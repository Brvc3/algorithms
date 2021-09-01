total = int(input())
safe = 0
for i in range(total):
    temp = input().split()
    w = (int(temp[0]))
    score = (int(temp[1]))
    safe += w*score
if safe>0:
    print(safe)
else:
    print(0)

