N=int(input())
arr=list(map(int,input().split()))
ycost=mcost=0
for i in range(N):
    ycost+=10*(1+arr[i]//30)
    mcost+=15*(1+arr[i]//60)
if ycost>mcost:
    print(f'M {mcost}')
elif ycost<mcost:
    print(f'Y {ycost}')
else:
    print(f'Y M {ycost}')