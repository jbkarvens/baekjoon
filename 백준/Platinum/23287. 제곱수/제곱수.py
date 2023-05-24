from random import randint
NUM=100000
pchklst=[True for _ in range(NUM)]
plst=[2]
j=2+2
while j<NUM:
    pchklst[j]=False
    j+=2
for i in range(3,NUM,2):
    if pchklst[i]:
        plst.append(i)
        j=i+i
        while j<NUM:
            pchklst[j]=False
            j+=i

def sum_of_four_squares(n):
    if n<NUM:
        for i in range(int((n/4)**0.5)+1):
            for j in range(i,int(((n-i*i)/3)**0.5)+1):
                for k in range(j,int(((n-i*i-j*j)/2)**0.5)+1):
                    t=int((n-i*i-j*j-k*k)**0.5)
                    if n==i*i+j*j+k*k+t*t:
                        return i,j,k,t
    for p in plst:
        if n%p==0:
            a1,a2,a3,a4=sum_of_four_squares(n//p)
            b1,b2,b3,b4=sum_of_four_squares(p)
            a=a1*b1-a2*b2-a3*b3-a4*b4
            b=a1*b2+a2*b1+a3*b4-a4*b3
            c=a1*b3-a2*b4+a3*b1+a4*b2
            d=a1*b4+a2*b3-a3*b2+a4*b1
            return abs(a),abs(b),abs(c),abs(d)

print(*sum_of_four_squares(int(input())))