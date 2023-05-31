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
lst=[]
h_str_dict=dict()
while True:
    s=rndstr(7)
    h=HAIKU(s,A,B)
    if h in h_str_dict:
        s2=h_str_dict[h]
        if s2==s:
            continue
        lst.append(s)
        lst.append(s2)
        break
    else:
        h_str_dict[h]=s
for i in range(100):
    s=''
    for j in range(7):
        s+=lst[(i>>j)%2]
    print(s)