N=int(input())
A=list(map(int,input().split()))
T,P=map(int, input().split())
tt=0
for a in A:
    tt+=(a+T-1)//T
print(tt)
print(N//P,N%P)