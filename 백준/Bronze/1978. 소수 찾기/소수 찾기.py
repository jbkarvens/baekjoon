def isPrime(num):
    if num<=1:
        return False
    elif num==2:
        return True
    if num%2==0:
        return False
    else:
        i=3
        while i*i<=num:
            if num%i==0:
                return False
            i+=2
    return True
N=int(input())
lst=list(map(int,input().split()))
print(sum([isPrime(num) for num in lst]))