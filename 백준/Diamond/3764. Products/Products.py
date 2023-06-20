import sys
input=sys.stdin.readline

import math

def dfs(u,v,d,c_now):
    if d>=ans[0]:
        return
    g=math.gcd(u,v)
    u,v=u//g,v//g
    if (u,v) in dp:
        if dp[(u,v)]<=d:
            return
        else:
            dp[(u,v)]=d
    if u+1==v:
        ans[0]=d+1
        return
    if u==v:
        ans[0]=d
        return
    if u>v:
        return
    if ans[0]==d+1:
        return
    c_next = math.ceil(u/(v-u))
    if u>10**6 or c_next>10**6:
        return
    if c_next<c_now:
        return
    while (ans[0]-d)*math.log(1+1/c_next)>=math.log(v/u):
        dfs(u*(c_next+1),v*c_next,d+1,c_next)
        c_next+=1
    return

if __name__=='__main__':
    N = int(input())
    dp=dict()
    ans = [20]
    dfs(1,N,0,1)
    print(ans[0])