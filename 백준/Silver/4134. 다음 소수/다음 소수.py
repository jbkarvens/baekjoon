def isPrime(num):
    if num<=1:
        return False
    elif num==2 or num==3:
        return True
    elif num%2==0 or num%3==0:
        return False
    i=5
    while i*i<=num:
        if num%i==0:
            return False
        if i%6==1:
            i+=4
        else:
            i+=2
    return True
N=int(input())
for _ in range(N):
    num=int(input())
    if num<=2:
        print(2)
    elif num==3:
        print(3)
    else:
        if num%2==0:
            num+=1
        if num%3==0:
            num+=2
        while not isPrime(num):
            if num%6==1:
                num+=4
            else:
                num+=2
        print(num)