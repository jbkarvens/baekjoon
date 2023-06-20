import sys
input = sys.stdin.readline

def kmp_fail(W):
    T=[0 for _ in range(len(W))]
    j=0
    for i in range(1,len(W)):
        while j>0 and W[i]!=W[j]:
            j=T[j-1]
        if W[i]==W[j]:
            T[i]=j+1
            j+=1
    return T

if __name__=='__main__':
    T = int(input())
    S = input().rstrip()
    res = kmp_fail(S)
    print(T-res[-1])