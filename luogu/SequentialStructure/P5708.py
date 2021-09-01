a,b,c = list(map(float,input().rstrip().split()))
p = 0.5*(a+b+c)
S = p*(p-a)*(p-b)*(p-c)
S = S**0.5
print("{:.1f}".format(S))