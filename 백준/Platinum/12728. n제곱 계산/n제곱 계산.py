lst=[2,6,28]
baby,giant=1,2
i=3
while True:
    i+=1
    if i%2==0:
        if lst[baby]==lst[giant] and lst[baby-1]==lst[giant-1]:
            break
        baby+=1
        giant+=2
    lst.append((lst[-1]*6-lst[-2]*4)%1000)
T=giant-baby
for i in range(1,len(lst)):
    if lst[i]==lst[baby] and lst[i-1]==lst[baby-1]:
        S=i
        break
for i in range(int(input())):
    n=int(input())
    if n<len(lst):
        m=(lst[n]-1)%1000
    else:
        m=(lst[S+(n-S)%T]-1)%1000
    mstr=str(m)
    while len(mstr)<3:
        mstr='0'+mstr
    print('Case #{}: '.format(i+1)+mstr)