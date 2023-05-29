N=int(input())
for i in range(N):
    s=''
    for _ in range(N-i-1): s+=' '
    for _ in range(2*i+1): s+='*'
    print(s)
for i in list(range(N-1))[::-1]:
    s=''
    for _ in range(N-i-1): s+=' '
    for _ in range(2*i+1): s+='*'
    print(s)