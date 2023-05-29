N=int(input())
lst_=[]
for _ in range(N):
    age_,name_=input().split()
    age_=int(age_)
    lst_.append([age_,name_])
sorted_lst_=sorted(lst_,key=lambda x:(x[0]))
for i in range(len(sorted_lst_)):
    print(*sorted_lst_[i])