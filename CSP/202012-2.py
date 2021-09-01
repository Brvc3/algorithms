total = int(input())
y = []
result = []
for i in range(total):
    temp = input().split()
    y.append((int(temp[0])))
    result.append((int(temp[1])))

#success = []

max = 0
index = 0
for theta in y:
    count = 0
    for j in range(total):
        if (y[j]>=theta and result[j] == 1)or(y[j]<theta and result[j] == 0):
            count += 1
    if count>max:
        max = count
        index = theta
    elif count == max:
        if theta>index:
            index = theta

print(index)
