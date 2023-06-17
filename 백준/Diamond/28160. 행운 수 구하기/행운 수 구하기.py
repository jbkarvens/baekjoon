import sys

# k+a*t<(a+1)*(lucky[j-t]-1)+1
def find(k, j, a):
    low = 0
    high = j
    while low<=high:
        mid = (low + high) // 2
        if k + a * mid < (a + 1)*(lucky[j - mid] - 1) + 1:
            low = mid + 1
        else:
            high = mid -1
    return high

def findlucky(k):
    low = 1
    high = len(lucky)
    while low<=high:
        mid = (low + high) // 2
        if lucky[mid] <= k:
            low = mid + 1
        else:
            high = mid - 1
    return high

def cal_lucky(M):
    if M<=200000:
        return lucky[M]
    j = findlucky(M)
    test = True
    lucky_k = M
    while j>=2:
        if test:
            a = (lucky_k-1)//(lucky[j]-1)
            jump=find(lucky_k, j, a)
            if jump == 0:
                test =False
                continue
            jump+=1
            lucky_k += jump * a
            j-=jump
        else:
            lucky_k += (lucky_k-1)//(lucky[j]-1)
            j-=1
    return 2*lucky_k-1

def solve(L,R):
    lucky_k = L
    j = findlucky(R)
    x_lst = [L]
    while j>=2:
        lucky_k +=(lucky_k-1)//(lucky[j]-1)
        x_lst.append(lucky_k)
        j-=1
    x_lst.reverse()
    U = cal_lucky(L)
    V = cal_lucky(R)
    new_lucky = list(range(U,V+2,2))
    for i in range(2,findlucky(R)+1):
        x = lucky[i]
        a = (-x_lst[i-2])%x
        if a<len(new_lucky):
            del new_lucky[a::x]
    return new_lucky

if __name__=='__main__':
    lucky = list(range(-1,3030000,2))
    for i in range(2,17000):
        x = lucky[i]
        del lucky[x::x]
    lucky = lucky[:200000+1]
    L,R = map(int,input().split())
    for lk in solve(L,R):
        print(lk)