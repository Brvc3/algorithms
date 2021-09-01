n,L,r,t = map(int,input().split())
graph = [[0 for i in range(n+1)]]
for i in range(n):
    graph.append([0]+list(map(int,input().split())))


#二维前缀和
sum = [[0 for i in range(n+1)] for i in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        sum[i][j] = graph[i][j] + sum[i-1][j] + sum[i][j-1] - sum[i-1][j-1]

count = 0
degree = 0

for i in range(1,n+1):
    for j in range(1,n+1):
        x_s,x_e = (max(1,i-r),min(n,i+r))
        y_s,y_e = (max(1,j-r),min(n,j+r))
        count = sum[x_e][y_e] - sum[x_e][y_s -1] - sum[x_s-1][y_e] +sum[x_s-1][y_s-1]
        all = (x_e - x_s + 1) * (y_e - y_s + 1)
        aver = count/all
        if aver <= t:
            degree += 1

print(degree)