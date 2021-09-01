m,t,s = list(map(float,input().rstrip().split()))
if t==0:
    print(0)
    exit(0)
left = int(m - s/t)
print(max(0,left))