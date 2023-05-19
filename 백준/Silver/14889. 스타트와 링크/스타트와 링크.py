N=int(input().rstrip())
S=[None for _ in range(N)]
for i in range(N):
    S[i]=list(map(int,input().split()))

team1=[None for _ in range(N//2)]
score=[100*N*N]

def dfs(d):
    if d==N//2:
        num=cal()
        if num<score[0]:
            score[0]=num
        return
    start=0
    if d>0:
        start=team1[d-1]+1
    for i in range(start,N//2+d+1):
        team1[d]=i
        dfs(d+1)
def cal():
    power_1=sum([S[team1[i]][team1[j]] for i in range(N//2) for j in range(N//2)])
    team2=[i for i in range(N) if not i in team1]
    power_2=sum([S[team2[i]][team2[j]] for i in range(N//2) for j in range(N//2)])
    return abs(power_1-power_2)
dfs(0)
print(score[0])