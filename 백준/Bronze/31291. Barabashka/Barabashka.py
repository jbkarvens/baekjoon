import sys
input=sys.stdin.readline

color=["white","blue","red","gray","green"]
itm=["Barabashka","book","chair","mouse","bottle"]
for _ in range(5):
    line=input().strip()
    for c in ["'",",","-","."]:
        line=line.replace(c,' ')
    sen=list(line.split())
    mycolor=[]
    myitm=[]
    for i in range(len(sen)-1):
        for j in range(5):
            if color[j]==sen[i]:
                mycolor.append(j)
                for k in range(5):
                    if itm[k]==sen[i+1]:
                        myitm.append(k)
                        break
                break
    suc=False
    for i in range(2):
        if mycolor[i]==myitm[i]:
            suc=True
            print(color[mycolor[i]],itm[myitm[i]])
            break
    if not suc:
        chk=[True]*5
        for i in range(2):
            chk[mycolor[i]]=False
            chk[myitm[i]]=False
        for i in range(5):
            if chk[i]:
                print(color[i],itm[i])
                break