n=int(input())
i,num=0,666
while True:
    tmp=num
    checker=False
    while tmp>100:
        if tmp%1000==666:
            checker=True
        tmp=tmp//10
    if checker:
        i+=1
    if i==n:
        print(num)
        break
    num+=1