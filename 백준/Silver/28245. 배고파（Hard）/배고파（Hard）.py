import sys
input=sys.stdin.readline

if __name__=='__main__':
    menu=[]
    for x in range(61):
        for y in range(x,61):
            menu.append([(1<<x)+(1<<y),(x,y)])
    menu.sort()
    n=int(input())
    for _ in range(n):
        m=int(input())
        low,high=0,len(menu)
        while low<=high:
            mid = (low+high)//2
            if menu[mid][0]<=m:
                low = mid+1
            else:
                high = mid-1
        if abs(m-menu[high][0])<=abs(m-menu[high+1][0]):
            print(*menu[high][1])
        else:
            print(*menu[high+1][1])