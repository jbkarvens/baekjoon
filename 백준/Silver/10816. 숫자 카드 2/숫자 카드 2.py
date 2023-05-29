import sys
input=sys.stdin.readline
N=int(input())
card_num=list(map(int,input().split()))
M=int(input())
q_num=list(map(int,input().split()))
card=dict()
for i in card_num:
    if i in card:
        card[i]+=1
    else:
        card[i]=1
ans=[]
for i in range(M):
    q=q_num[i]
    ans.append(card.get(q,0))
print(*ans)