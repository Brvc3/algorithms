total = int(input())
man = []
for i in range(total):
    man.append(list(map(int,input().split())))#[y,result]

man.sort(key = lambda x:x[1],reverse = True)#1在前
man.sort(key = lambda x:x[0])#y
#print(man)

success = []

#统计各元素之前的0数量
count = 0
for i in range(total):
    success.append(count) 
    if man[i][1] == 0:
        count += 1

#统计各元素之后的1数量
count = 0
for i in range(total-1,-1,-1):
    if man[i][1] == 1:
        count += 1
    success[i] += count

success.reverse()
index = total - 1 - success.index(max(success))

print(man[index][0])