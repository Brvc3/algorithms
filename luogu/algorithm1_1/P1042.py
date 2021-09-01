def eleven(info):
    plays = len(info)//11 + 1
    i = 0
    for i in range(plays-1):
        win = info[i*11:i*11+11].count('W')
        print('%d:%d'%(win,11-win))
    i+=1
    win = info[i*11:i*11+11].count('W')
    print('%d:%d'%(win,len(info)-11*i-win))

def twone(info):
    plays = len(info)//21 + 1
    i = 0
    for i in range(plays-1):
        win = info[i*21:i*21+21].count('W')
        print('%d:%d'%(win,21-win))
    i+=1
    win = info[i*21:i*21+21].count('W')
    print('%d:%d'%(win,len(info)-21*i-win))

info = ''
i = 0;
while(1): 
    info += (input().rstrip())
    idx = info.rfind('E')
    if  idx != -1:
        info = info[:idx]
        break

eleven(info)
print('')
twone(info)

