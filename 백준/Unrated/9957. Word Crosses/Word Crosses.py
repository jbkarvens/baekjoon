import sys
input_func=sys.stdin.readline

def P_9957(s1,s2,s3,s4):
    lst1,lst2=[0 for _ in range(26)],[0 for _ in range(26)]
    score1,score2=[0 for _ in range(26)],[0 for _ in range(26)]
    u1,u2,u3,u4=-1,-1,-1,-1
    checker=False
    doublechecker=True
    for i in range(26):
        t1,t2=False,False
        p1,p2=0,0
        for c in range(len(s1)):
            if i+ord('A')==ord(s1[c]):
                t1,p1=True,c
                break
        for c in range(len(s2)):
            if i+ord('A')==ord(s2[c]):
                t2,p2=True,c
                break
        if t1 and t2:
            lst1[i]=[p1,p2]
            score1[i]=1/(p1+p2+2)
            checker=True
    if checker:
        u1=lst1[score1.index(max(score1))][0]
        u2=lst1[score1.index(max(score1))][1]
    else:
        doublechecker=False
        
    checker=False
    for i in range(26):
        t1,t2=False,False
        p1,p2=0,0
        for c in range(len(s3)):
            if i+ord('A')==ord(s3[c]):
                t1,p1=True,c
                break
        for c in range(len(s4)):
            if i+ord('A')==ord(s4[c]):
                t2,p2=True,c
                break
        if t1 and t2:
            lst2[i]=[p1,p2]
            score2[i]=1/(p1+p2+2)
            checker=True
    if checker:
        u3=lst2[score2.index(max(score2))][0]
        u4=lst2[score2.index(max(score2))][1]
    else:
        doublechecker=False
    if not doublechecker:
        return ['Unable to make two crosses']
    else:
        lst=[[' ' for _ in range(len(s1)+3+len(s3))] for _ in range(max(u2,u4)+1+max(len(s2)-1-u2,len(s4)-1-u4))]
        if u2>=u4:
            for i in range(len(s2)):
                lst[i][u1]=s2[i]
            for i in range(len(s4)):
                lst[u2-u4+i][len(s1)+3+u3]=s4[i]
        else:
            for i in range(len(s2)):
                lst[u4-u2+i][u1]=s2[i]
            for i in range(len(s4)):
                lst[i][len(s1)+3+u3]=s4[i]
        for i in range(len(s1)):
            lst[max(u2,u4)][i]=s1[i]
        for i in range(len(s3)):
            lst[max(u2,u4)][i+len(s1)+3]=s3[i]
    for k in range(len(lst)):
        tmp=[]
        line=lst[k]
        stoppt=len(line)-1
        for i in range(len(line)):
            if line[len(line)-i-1]!=' ':
                stoppt=len(line)-i
                break
        for i in range(stoppt):
            tmp.append(line[i])
        lst[k]=tmp
    return lst

if __name__=='__main__':
    ans=[]
    outsen=''
    while True:
        sen=input_func()
        if sen[0]=='#':
            break
        else:
            s1,s2,s3,s4=sen.split()
            ans.append(P_9957(s1,s2,s3,s4))

    for lst in ans:
        for i in range(len(lst)):
            outsen=outsen+''.join(lst[i])
            outsen=outsen+'\n'
        outsen=outsen+'\n'
    print(outsen[:-1])