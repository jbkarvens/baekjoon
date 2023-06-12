import sys
input_func = sys.stdin.readline

if __name__=='__main__':
    Q,M = map(int,input_func().split())
    fib_lst = [0,1]
    fib_str ='01'
    a,b=1,1
    while True:
        a,b=b,(a+b)%M
        if a==0 and b==1:
            break
        fib_lst.append(a)
        fib_str+=str(a)
    mod = len(fib_str)
    for _ in range(Q):
        N = int(input_func())
        sys.stdout.write(f'{fib_str[N%mod]}\n')