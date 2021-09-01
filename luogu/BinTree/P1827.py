class node:
    

DLR_raw = input().rstrip()
LDR_raw = input().rstrip()
DLR = []
LDR = []
for i in range(len(DLR_raw)):
    DLR.append(DLR_raw[i])
    LDR.append(LDR_raw[i])

output = []
i = 0
while(1):
    rootidx = LDR.index(DLR[i])
    output.append(rootidx)

    
    
