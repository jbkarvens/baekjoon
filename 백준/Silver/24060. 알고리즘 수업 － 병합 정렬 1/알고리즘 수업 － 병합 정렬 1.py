# -*- coding: utf-8 -*-
"""
Created on Mon May 15 13:29:09 2023

@author: LG
"""
progress=[]
def merge_sort(A,p,r):
    if p<r:
        q=(p+r)//2
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)
def merge(A,p,q,r):
    i,j,t=p,q+1,0
    tmp=[None for _ in list(range(r-p+1))]
    while i<=q and j<=r:
        if A[i]<=A[j]:
            tmp[t]=A[i]
            t+=1
            i+=1
        else:
            tmp[t]=A[j]
            t+=1
            j+=1
    while i<=q:
        tmp[t]=A[i]
        t+=1
        i+=1
    while j<=r:
        tmp[t]=A[j]
        t+=1
        j+=1
    for i in range(p,r+1):
        A[i]=tmp[i-p]
        progress.append(A[i])
N,K=map(int,input().split())
A=list(map(int,input().split()))
merge_sort(A,0,len(A)-1)
if K>len(progress):
    print(-1)
else:
    print(progress[K-1])