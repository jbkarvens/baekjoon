N=int(input())
sen=input().strip()
cnt=0
for i in range(N//2):
    if sen[i]!=sen[N-i-1]:
        cnt+=1
print(cnt)