N=int(input())
lst=[None for _ in range(N+1)]
lst[1]=0
for i in range(2,N+1):
    search_index=[i-1]
    if i%3==0: search_index.append(i//3)
    if i%2==0: search_index.append(i//2)
    lst[i]=min([lst[j] for j in search_index])+1
print(lst[N])