import sys
input=sys.stdin.readline

def work(n):
    plst = [True for _ in range(n+1)]
    omega = [0 for _ in range(n+1)]
    for p in range(2,n+1):
        if plst[p]:
            omega[p]=1
            for i in range(p+p,n+1,p):
                omega[i]=omega[i//p]+1
                plst[i] = False
    L_dict[0]=0
    res = 0
    for i in range(1,n+1):
        if omega[i]&1:
            res-=1
        else:
            res+=1
        L_dict[i] = res

def L(n):
    if n in L_dict:
        return L_dict[n]
    res = int(n**0.5)
    a=n//2
    while a>=1:
        res-=L(a)*(n//a-n//(a+1))
        a=n//((n//a) + 1)
    
    L_dict[n] = res
    return res

if __name__=='__main__':
    L_dict={}
    for _ in range(int(input())):
        n = int(input())
        if n<906150257 or n>906488079:
            if n==1:
                sys.stdout.write('E\n')
            else:
                sys.stdout.write('O\n')
        else:
            if L(n)>0:
                sys.stdout.write('E\n')
            else:
                sys.stdout.write('O\n')