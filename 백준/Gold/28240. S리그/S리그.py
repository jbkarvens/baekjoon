import sys
input=sys.stdin.readline
import math

if __name__=='__main__':
    n=int(input())
    H=10**5
    A=[*map(int,input().split())]
    for i in range(len(A)):
        A[i]-=1
    A.sort()
    coor=[[] for _ in range(n)]
    coor[A[0]]=[0,0]
    i=(A[0]+1)%n
    x=1
    while i!=A[1]:
        coor[i]=[x,0]
        x+=1
        i=(i+1)%n
    coor[A[1]]=[x+1,-1]
    x,y=H,0
    i=(A[1]+1)%n
    while i!=A[2]:
        coor[i]=[x,y]
        x,y=x-1,y+1
        i=(i+1)%n
    coor[A[2]]=[0,H]
    x,y=-1,H-1
    i=(A[2]+1)%n
    while i!=A[3]:
        coor[i]=[x,y]
        x,y=x-1,y-1
        i=(i+1)%n
    i=(A[0]-1)%n
    x=-1
    while i!=A[3]:
        coor[i]=[x,0]
        x-=1
        i=(i-1)%n
    coor[A[3]]=[x-1,-1]
    for xy in coor:
        print(*xy)