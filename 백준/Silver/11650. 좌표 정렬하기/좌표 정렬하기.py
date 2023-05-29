N=int(input())
list_=[]
for _ in range(N):
    list_.append(list(map(int,input().split())))
lexico_sorted_list_=sorted(list_,key=lambda x:(x[0],x[1]))
for i in range(N):
    print(*lexico_sorted_list_[i])