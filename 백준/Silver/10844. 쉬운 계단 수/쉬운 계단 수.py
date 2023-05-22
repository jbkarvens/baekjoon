N=int(input())
M=10**9
# val[i][j]: 길이가 i+1이고 j로 끝나는 계단 수 갯수
val=[[1 for _ in range(10)]]
val[0][0]=0
for i in range(1,N):
    lst=[None for _ in range(10)]
    for j in range(1,9):
        lst[j]=(val[i-1][j+1]+val[i-1][j-1])%M
    lst[0]=val[i-1][1]
    lst[9]=val[i-1][8]
    val.append(lst)
print(sum(val[N-1])%M)