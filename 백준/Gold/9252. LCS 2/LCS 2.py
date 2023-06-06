import sys
input=sys.stdin.readline

s1=input().rstrip()
s2=input().rstrip()
n1,n2=len(s1),len(s2)
dp_current=['' for _ in range(n2+1)]
dp_before=['' for _ in range(n2+1)]
for i in range(1,n1+1):
    for j in range(1,n2+1):
        if s1[i-1]==s2[j-1]:
            dp_current[j]=dp_before[j-1]+s1[i-1]
        else:
            if len(dp_before[j])>len(dp_current[j-1]):
                dp_current[j]=dp_before[j]
            else:
                dp_current[j]=dp_current[j-1]
    dp_before=dp_current[:]
    do_current=[[] for _ in range(n2+1)]
print(len(dp_before[-1]))
print(dp_before[-1])