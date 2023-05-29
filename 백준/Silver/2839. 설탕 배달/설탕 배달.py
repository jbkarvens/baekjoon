N=int(input())
count=0
while True:
    if N%5==0:
        if N>=0:
            count+=N//5
        else:
            count=-1
        break
    N-=3
    count+=1
print(count)