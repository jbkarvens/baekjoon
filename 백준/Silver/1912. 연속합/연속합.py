n=int(input())
lst=list(map(int,input().split()))
def dp():
    tot_max,right_max=0,0
    if all(val<0 for val in lst):
        tot_max=max(lst)
        return tot_max
    for i in range(n):
        if lst[i]>=0 or lst[i]+right_max>=0:
            right_max+=lst[i]
        else:
            right_max=0
        if right_max>tot_max:
            tot_max=right_max
    return tot_max
print(dp())