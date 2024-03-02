n = int(input())
comlist=[]
for i in range(1, n+1): 
    command = input()
    comlist.append(command)
spisok = []
for j in range (0, len(comlist)):
    
    com = comlist[j]
    if (com.split())[0]=='insert' and len(com.split())==3:
        a = com.split()
        spisok.insert(int(a[1]),int(a[2]))
        
    elif (com.split())[0]=='append' and len(com.split())==2: 
        spisok.append(int((com.split())[1]))
    
    elif (com.split())[0]=='remove' and len(com.split())==2: 
        spisok.remove(int((com.split())[1]))
    
    elif (com.split())[0]=='sort' and len(com.split())==1:
        spisok.sort()

    elif (com.split())[0]=='print' and len(com.split())==1:
        print(spisok)

    elif (com.split())[0]=='reverse' and len(com.split())==1:
        spisok.reverse()

    elif (com.split())[0]=='pop' and len(com.split())==1:
        spisok.pop()