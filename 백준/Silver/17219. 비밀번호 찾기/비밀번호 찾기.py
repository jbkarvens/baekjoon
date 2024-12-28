import sys
input=sys.stdin.readline

N,M=map(int,input().split())
pwd=dict()
for _ in range(N):
    site,pw=input().split()
    pwd[site]=pw
for _ in range(M):
    site=input().strip()
    print(pwd[site])