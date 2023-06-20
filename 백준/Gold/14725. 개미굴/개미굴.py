import sys
input = sys.stdin.readline

def show(node,depth):
    if node!=0:
        for _ in range(depth):
            print('--',end='')
        print(graph[node][0])
    tmp = [[graph[nextnode][0],nextnode] for nextnode in graph[node][2]]
    tmp.sort()
    for _,nextnode in tmp:
        show(nextnode,depth+1)

if __name__=='__main__':
    graph=[[None,[],[]]]
    last = 1
    for _ in range(int(input())):
        k=0
        q=input().split()
        for i in range(1,int(q[0])+1):
            s=q[i]
            if s in graph[k][1]:
                k=graph[k][2][graph[k][1].index(s)]
            else:
                graph[k][1].append(s)
                graph[k][2].append(last)
                k = last
                last+=1
                graph.append([s,[],[]])
    show(0,-1)