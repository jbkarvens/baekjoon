import sys
input=sys.stdin.readline

# https://susam.net/blog/langford-pairing.html
def solve(N):
    if N==1:
        return [0,0]
        
    m = N-1
    if m%4==0:
        x = m//4
    elif m%4==3:
        x=(m+1)//4
    else:
        return None
    a = 2*x-1
    b = 4*x-2
    c = 4*x-1
    d = 4*x
    p=list(range(1,a,2))
    q=list(range(2,a,2))
    r=list(range(a+2,b,2))
    s=list(range(a+1,b,2))
    result = []
    if m%4==0:
        result = s[::-1]+p[::-1]+[b]+p+[c]+s+[d]+r[::-1]+q[::-1]+[b,a]+q+[c]+r+[a,d]+[0,0]
    elif m%4==3:
        result = s[::-1]+p[::-1]+[b]+p+[c]+s+[a]+r[::-1]+q[::-1]+[b,a]+q+[c]+r+[0,0]
    return result

if __name__=='__main__':
    N = int(input())
    ans = solve(N)
    if ans==None:
        sys.stdout.write('No\n')
    else:
        sys.stdout.write('Yes\n')
        for i,v in enumerate(ans):
            if i!=0:
                sys.stdout.write(' ')
            sys.stdout.write(str(v))
        sys.stdout.write('\n')