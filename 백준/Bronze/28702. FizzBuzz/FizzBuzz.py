A=[input().strip(),input().strip(),input().strip()]
s35='FizzBuzz'
s3='Fizz'
s5='Buzz'
i=0
while i<3:
    if A[i]!=s35 and A[i]!=s3 and A[i]!=s5:
        break
    i+=1
num=int(A[i])+3-i
t3=num%3==0
t5=num%5==0
if t3:
    if t5:
        print(s35)
    else:
        print(s3)
else:
    if t5:
        print(s5)
    else:
        print(num)