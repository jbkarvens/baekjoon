import sys
input=sys.stdin.readline
for _ in range(int(input())):
    s=input().rstrip()
    score=0
    c=0
    for i in range(len(s)):
        if s[i]=='O':
            c+=1
            score+=c
        else:
            c=0
    print(score)