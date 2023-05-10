N=int(input())
keyname_='ChongChong'
dancers=set()
dancers.add(keyname_)
for _ in range(N):
    A,B=input().split()
    if A in dancers or B in dancers:
        dancers.add(A)
        dancers.add(B)
print(len(dancers))