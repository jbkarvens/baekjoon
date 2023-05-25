def isPrime(n):
    if n<=1:
        return False
    if n==2:
        return True
    i=3
    while i*i<=n:
        if n%i==0:
            return False
        i+=2
    return True

if __name__=='__main__':
    k=(500-1)//6
    while True:
        if isPrime(6*k+1) and isPrime(12*k+1) and isPrime(18*k+1):
            n=(6*k+1)*(12*k+1)*(18*k+1)
            print(n,6*k+1)
            break
        k+=1