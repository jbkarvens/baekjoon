import sys
input = sys.stdin.readline

class Node:
    def __init__(self,end=False):
        self.end = end
        self.child = {}

def add(start,word):
    cur_node = start
    for c in word:
        if c not in cur_node.child:
            cur_node.child[c] = Node()
        cur_node = cur_node.child[c]
    cur_node.end = True

def find(start,word):
    cur_node = start
    for c in word:
        if c not in cur_node.child:
            return False
        cur_node = cur_node.child[c]
    return cur_node.end

if __name__=='__main__':
    start = Node()
    N,M=map(int,input().split())
    for _ in range(N):
        add(start,input().rstrip())
    ans = 0
    for _ in range(M):
        if find(start,input().rstrip()):
            ans+=1
    print(ans)