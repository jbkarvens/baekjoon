import sys
input=sys.stdin.readline


# 1-p^u+p^v=0 mod
def find_collision(p):
    mod = 10**9+7
    odds=dict()
    root = int(2*int(mod**0.5))+1
    if p in [29,37,43,47,53,61,67]:
        for i in range(1,root):
            odds[(-1+pow(p,i,mod))%mod]=i
        for i in range(1,root):
            a = pow(p,i,mod)
            if a in odds:
                if odds[a]==i:
                    continue
                return [[0,1],[odds[a],-1],[i,1]]
    elif p in [31,59]:
        for i in range(1,root):
            odds[(-1-pow(p,i,mod))%mod]=i
        for i in range(1,root):
            a = pow(p,i,mod)
            if a in odds:
                if odds[a]==i:
                    continue
                return [[0,1],[odds[a],1],[i,1]]
    elif p in [41]:
        for i in range(1,root):
            odds[(1+pow(p,i,mod))%mod]=i
        for i in range(1,root):
            a = pow(p,i,mod)
            if a in odds:
                if odds[a]==i:
                    continue
                return [[0,1],[odds[a],1],[i,-1]]

def poly_mult(f,g):
    h = []
    for x in f:
        for y in g:
            h.append([x[0]+y[0],x[1]*y[1]])
    return h

def hsh(sen,p):
    mod = 10**9+7
    res=0
    pp=1
    for c in sen:
        res+=pp*ord(c)
        pp=(p*pp)%mod
    return res%mod

if __name__=="__main__":
    # degree,coefficiet
    poly=[[0,1]]
    
    prime_list = [29,31,37,41,43,47,53,59,61,67]
    for p in prime_list:
        poly = poly_mult(poly,find_collision(p))
    deg=max([x[0] for x in poly])
    real_poly=[0 for _ in range(deg+1)]
    for x in poly:
        real_poly[x[0]]+=x[1]
    low=min(real_poly)
    s1,s2=[],[]
    for c in real_poly:
        s1.append(chr(-low+ord('a')))
        s2.append(chr(c-low+ord('a')))
    
    # test
    # print(len(s1))
    # for p in prime_list:
    #     print(hsh(s1,p)-hsh(s2,p))
    
    # print
    sys.stdout.write(''.join(s1)+'\n')
    sys.stdout.write(''.join(s2)+'\n')