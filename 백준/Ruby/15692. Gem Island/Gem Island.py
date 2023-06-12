import sys
import math
input_func = sys.stdin.readline

n,d,r=map(int,input_func().split())

# exp[people][day] : day일 후 상위 r명의 gem수의 expectation(사람 수=people)
exp = [[None for _ in range(d+1)] for _ in range(n+1)]
for i in range(d+1):
    exp[r][i] = float(i)
for i in range(n+1):
    exp[i][0] = float(0)

N_MAX = 1000
binom = [[0 for _ in range(N_MAX+1)] for _ in range(N_MAX+1)]
for i in range(N_MAX+1):
    binom[i][0] = 1.0
    binom[i][i] = 1.0
    for j in range(1,i):
        binom[i][j] = binom[i-1][j] + binom[i-1][j-1]

for peop in range(r+1,n+1):
    for day in range(1,d+1):
        res = 0
        # poor : peop명 중 최소 gem 값
        # cout : poor만큼의 gem 가진 사람 수
        for i in range(day+1):
            poor = i//peop
            cout = peop - i%peop
            prob = binom[peop][cout]*binom[day-peop*poor-1][peop-cout-1]
            if cout>=peop-r:
                gems = day - (peop - r)*poor
            else:
                gems = exp[peop-cout][day-(1+poor)*peop+cout] + r*(poor+1)
            res+=gems*prob
        exp[peop][day] = res/binom[peop+day-1][day]

print(exp[n][d]+r)