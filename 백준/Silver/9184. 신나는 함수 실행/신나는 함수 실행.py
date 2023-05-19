def cal_w(a,b,c):
    if a<=0 or b<=0 or c<=0:
        return 1
    if a>20 or b>20 or c>20:
        a=b=c=20
    w=[[[None for _ in range(c+1)] for _ in range(b+1)] for _ in range(a+1)]
    for i in range(a+1):
        for j in range(b+1):
            for k in range(c+1):
                if i==0 or j==0 or k==0:
                    w[i][j][k]=1
    for i in range(1,a+1):
        for j in range(1,b+1):
            for k in range(1,c+1):
                if i<j<k:
                    w[i][j][k]=w[i][j][k-1]+w[i][j-1][k-1]-w[i][j-1][k]
                else:
                    w[i][j][k]=w[i-1][j][k]+w[i-1][j-1][k]+w[i-1][j][k-1]-w[i-1][j-1][k-1]
    return w[a][b][c]

while True:
    a,b,c=map(int,input().split())
    if a==b==c==-1:
        break
    print('w({0}, {1}, {2}) = {3}'.format(a,b,c,cal_w(a,b,c)))