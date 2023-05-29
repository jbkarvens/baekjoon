N=int(input())
list_=[]
for _ in range(N):
    list_.append(input())
sorted_list_=sorted(list_,key=lambda x:(len(x),x))
sorted_list_=list(dict.fromkeys(sorted_list_))
for i in range(len(sorted_list_)):
    print(sorted_list_[i])
