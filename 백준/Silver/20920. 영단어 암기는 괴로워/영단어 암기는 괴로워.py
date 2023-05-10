import sys
input=sys.stdin.readline
N,M=map(int,input().split())
mydict={}
for _ in range(N):
    word_=input().rstrip()
    if len(word_)>=M:
        if word_ in mydict:
            mydict[word_]+=1
        else:
            mydict[word_]=1
mylst=[]
for w in mydict:
    mylst.append([w,mydict[w]])
mylst=sorted(mylst,key=lambda x:(-x[1],-len(x[0]),x[0]))
for i in range(len(mylst)):
    print(mylst[i][0])