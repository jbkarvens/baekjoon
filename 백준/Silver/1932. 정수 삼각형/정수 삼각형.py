n=int(input())
# 맨 아래줄에서 k번째 노드를 선택했을 때 최댓값은 max_list[k]
max_list=[0 for _ in range(n)]

for i in range(n):
    lst=list(map(int,input().split()))
    tmp=max_list[:]
    tmp[0]+=lst[0]
    for k in range(1,i+1):
        tmp[k]=max(max_list[k-1],max_list[k])+lst[k]
    for i in range(n):
        max_list[i]=tmp[i]
print(max(max_list))