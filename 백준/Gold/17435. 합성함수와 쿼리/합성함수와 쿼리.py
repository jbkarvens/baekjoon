import sys
input=sys.stdin.readline

if __name__=='__main__':
    M = int(input())
    F = [None]+[*map(int, input().split())]
    sparse_table = [[F[i]] for i in range(M + 1)]
    depth = 20
    for i in range(depth):
        for j in range(1,M+1):
            sparse_table[j].append(sparse_table[sparse_table[j][i]][i])
    
    for _ in range(int(input())):
        n,x=map(int, input().split())
        for i in reversed(range(depth)):
            if n&(1<<i)!=0:
                x = sparse_table[x][i]
            n&=~(1<<i)
        print(x)