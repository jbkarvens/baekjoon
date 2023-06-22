import sys
input=sys.stdin.readline

if __name__=='__main__':
    n=int(input())
    for _ in range(n):
        m=int(input())
        x=0
        while not m&1:
            m>>=1
            x+=1
        m-=1
        y=x
        if m==0:
            y-=1
            x-=1
        else:
            while not m&1:
                m>>=1
                y+=1
        sys.stdout.write(f'{x} {y}\n')