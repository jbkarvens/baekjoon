N=int(input())
myMaker=N+1
for num in range(max(1,N-100),N):
    tmp=num
    digitsum=0
    while tmp>=10:
        digitsum+=tmp%10
        tmp=tmp//10
    if tmp>0:
        digitsum+=tmp
    if digitsum+num==N:
        myMaker=num
        break
if myMaker==N+1:
    print(0)
else:
    print(myMaker)