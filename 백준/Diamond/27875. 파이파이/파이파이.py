import sys
input=sys.stdin.readline

def bbp_term(n,t):
    eps=pow(10,-5)
    result = 0
    for k in range(n+1):
        m = (8*k+t)**2
        result += pow(16,n-k,16*m)/m
    k = n+1
    result_back = 0
    while True:
        m=(8*k+t)**2
        temp=result_back+pow(16,n-k)/m
        if (temp-result_back)<eps:
            break
        result_back=temp
        k+=1
    return result+result_back

def bbp(n):
    result = 0
    coeff=[0,8,-8,-4,-8,-2,-2,1]
    for i in range(1,8):
        if coeff[i]==0:
            continue
        result+=coeff[i]*bbp_term(n,i)
    result*=2
    return result%16

if __name__=='__main__':
    n=int(input())
    print(hex(int(bbp(n))).upper()[-1])