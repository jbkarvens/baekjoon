s=input().strip()
ss=''
for c in s:
    if ord('a')<=ord(c)<=ord('z'):
        ss+=chr(ord(c)-ord('a')+ord('A'))
    else:
        ss+=chr(ord(c)-ord('A')+ord('a'))
print(ss)  