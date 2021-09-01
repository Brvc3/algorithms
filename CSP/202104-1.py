n,m,L = map(int,input().split())
l = [0 for i in range(L)]

for i in range(n):
    temp = list(map(int,input().split()))
    for i in range(m):
        l[temp[i]] += 1

for i in range(L):
    print(l[i],end = ' ')
