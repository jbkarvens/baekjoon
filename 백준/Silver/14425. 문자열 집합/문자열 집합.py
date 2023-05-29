def BinSearch(arr,tar):
    a,b=0,len(arr)-1
    m=(a+b)//2
    while a<=b:
        if arr[m]<tar:
            a=m+1
            m=(a+b)//2
        elif arr[m]>tar:
            b=m-1
            m=(a+b)//2
        else:
            return m
    return None
N,M=map(int,input().split())
lst_S=[]
for _ in range(N):
    lst_S.append(input())
lst_test=[]
for _ in range(M):
    lst_test.append(input())
lst_S.sort()
cout=0
for tar in lst_test:
    if BinSearch(lst_S,tar) is not None:
        cout+=1
print(cout)