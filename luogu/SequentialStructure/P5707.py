s,v = map(int,input().split())
time = s//v
if s%v != 0:
    time += 1
time += 10
hour = 7-time//60
quar = 60-time%60
if quar == 60:
    hour += 1
    quar = 0
if hour<0:
    hour += 24
print("%02d:%02d"%(hour,quar))