sen=input()
ans=0
s=''
idx=len(sen)-1
if '-' in sen:
    idx=sen.index('-')
for i in range(idx+1):
    if sen[i]=='+' or sen[i]=='-':
        ans+=int(s)
        s=''
    else:
        s+=sen[i]
if s!='':
    ans+=int(s)
s=''
for i in range(idx+1,len(sen)):
    if sen[i]=='-' or sen[i]=='+':
        ans-=int(s)
        s=''
    else:
        s+=sen[i]
if s!='':
    ans-=int(s)
print(ans)