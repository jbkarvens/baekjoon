count=[0,0]
def fib(n):
    if n==1 or n==2:
        count[0]+=1
        return 1
    else: return fib(n-1)+fib(n-2)
def fibonacci(n):
    f=[None,1,1]
    for i in range(3,n+1):
        f.append(f[i-1]+f[i-2])
        count[1]+=1
    return f[n]
n=int(input())
fib(n)
fibonacci(n)
print(*count)