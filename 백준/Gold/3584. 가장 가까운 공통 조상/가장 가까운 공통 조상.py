import sys
input=sys.stdin.readline

if __name__=='__main__':
    for _ in range(int(input())):
        N = int(input())
        parent = [[] for _ in range(N+1)]
        for _ in range(N-1):
            a,b=map(int, input().split())
            parent[b].append(a)
        x,y=map(int, input().split())
        parent_of_x=set()
        lst=parent[x]
        parent_node = x
        while lst:
            parent_of_x.add(parent_node)
            parent_node=lst[0]
            lst=parent[parent_node]
        current_node = y
        lst=parent[current_node]
        while lst:
            if current_node in parent_of_x:
                break
            current_node = lst[0]
            lst=parent[current_node]
        print(current_node)