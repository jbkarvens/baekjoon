import random
def rndstr(n):
    s=''
    for _ in range(n):
        s+=chr(random.randint(0,25)+ord('a'))
    return s
def HAIKU(s,A,B):
    h=0
    for i in range(len(s)):
        h=(h*A+ord(s[i])-ord('a')+1)%B
    return h
A,B=map(int,input().split())
chk=set()
lst=[]
while len(lst)<7:
    h_str_dict=dict()
    while True:
        s=rndstr(7)
        if s in chk:
            continue
        h=HAIKU(s,A,B)
        if h in h_str_dict:
            s2=h_str_dict[h]
            if s2==s:
                continue
            chk.add(s)
            chk.add(s2)
            lst.append([s,s2])
            break
        else:
            h_str_dict[h]=s
for i in range(100):
    s=''
    for j in range(7):
        s+=lst[j][(i>>j)%2]
    print(s)