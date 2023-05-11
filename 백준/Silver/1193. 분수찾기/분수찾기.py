import math
X=int(input())
k=math.ceil((2*X+1/4)**0.5+1/2)-1
r=X-(k-1)*k//2
if k%2==0:
    print('{0}/{1}'.format(r,k+1-r))
else:
    print('{0}/{1}'.format(k+1-r,r))