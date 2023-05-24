cout_two_squares=[None for i in range(2**15+1)]

def cal_two_squares():
    cout_two_squares[0]=set()
    for n in range(1,2**15+1):
        sqdict=set()
        for j in range(1,int((n/2)**0.5)+1):
            if isSquare(n-j*j):
                sqdict.add((j,int((n-j*j)**0.5)))
        cout_two_squares[n]=sqdict

def isSquare(n):
    if n==int(n**0.5)**2:
        return True
    return False
def count_squares(n):
    sqdict=set()
    if isSquare(n):
        sqdict.add((n,))
        
    for e in cout_two_squares[n]:
        sqdict.add(e)
        
    for i in range(1,int((n/3)**0.5)+1):
        for j,k in cout_two_squares[n-i*i]:
            tmp=sorted([i,j,k])
            sqdict.add((tmp[0],tmp[1],tmp[2]))
    
    for i in range(1,int((n/4)**0.5)+1):
        for j in range(i,int(((n-i*i)/3)**0.5)+1):
            for k1,k2 in cout_two_squares[n-i*i-j*j]:
                tmp=sorted([i,j,k1,k2])
                sqdict.add((tmp[0],tmp[1],tmp[2],tmp[3]))
    return len(sqdict)

if __name__=='__main__':
    cal_two_squares()
    while True:
        n=int(input())
        if n==0:
            break
        print(count_squares(n))