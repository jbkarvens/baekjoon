import sys
input=sys.stdin.readline

n = int(input().strip())
seq = list(map(int,input().split()))
A = 30000
# t = aj-ai = ak-aj
n_left = [0 for _ in range(A+1)]
n_right = [0 for _ in range(A+1)]
res = 0
for i in range(1,n):
    n_right[seq[i]]+=1
for j in range(1,n-1):
    aa = seq[j]
    n_left[seq[j-1]]+=1
    n_right[aa]-=1
    for t in range(max(aa-A,1-aa),1+min(aa-1,A-aa)):
        res += n_left[aa-t]*n_right[aa+t]
print(res)