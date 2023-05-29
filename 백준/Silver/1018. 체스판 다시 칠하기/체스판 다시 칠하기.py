N,M=map(int,input().split())
lst=[]
for _ in range(N):
    line=input()
    lst.append([line[i] for i in range(len(line))])
myColor=64
for i in range(N-8+1):
    for j in range(M-8+1):
        count=0
        for x in range(8):
            for y in range(8):
                if (x+y)%2==0 and lst[i+x][j+y]=='W':
                    count+=1
                elif (x+y)%2==1 and lst[i+x][j+y]=='B':
                    count+=1
        if min(count,64-count)<myColor:
            myColor=min(count,64-count)
print(myColor)