import sys
input_func = sys.stdin.readline

n,d,r=map(int,input_func().split())

# gem[people][day] : 가능한 조합에서 day일 후 상위 r명의 gem수들 합(사람 수=people)
gem = [[None for _ in range(d+1)] for _ in range(n+1)]

N_MAX = 1000
binom = [[0 for _ in range(N_MAX+1)] for _ in range(N_MAX+1)]
for i in range(N_MAX+1):
    binom[i][0] = 1.0
    binom[i][i] = 1.0
    for j in range(1,i):
        binom[i][j] = binom[i-1][j] + binom[i-1][j-1]

for i in range(r,n+1):
    gem[i][0] = float(r)
for i in range(d+1):
    for j in range(r+1):
        gem[j][i] = float(i+j)*binom[i+j-1][i]

for peop in range(r+1,n+1):
    for day in range(0,d+1):
        res = 0
        # i : gem들 나눠줬을 때 기본 gem 하나만 가진 사람 수
        for i in range(max(0,peop-day),peop+1):
            res += binom[peop][i] * gem[peop - i][day - peop + i]
        gem[peop][day] = res + r*binom[peop+day-1][day]

print(gem[n][d]/binom[n+d-1][d])