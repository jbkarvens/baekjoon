s=input()
lst=[0]*26
for i in range(len(s)):
    if ord(s[i])>=ord('a') and ord(s[i])<=ord('z'):
        lst[ord(s[i])-ord('a')]+=1
    else:
        lst[ord(s[i])-ord('A')]+=1
m=max(lst)
if lst.count(m)>1:
    print('?')
else:
    print(chr(ord('A')+lst.index(m)))