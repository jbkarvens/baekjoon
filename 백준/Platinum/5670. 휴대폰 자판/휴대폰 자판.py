import sys
input = sys.stdin.readline

class Node:
    def __init__(self,end=False):
        self.end = end
        self.child = {}

def add(start,word,mode=False):
    cur_node = start
    for c in word:
        if c not in cur_node.child:
            cur_node.child[c] = Node()
        cur_node = cur_node.child[c]
    cur_node.end = True

def find(start,word):
    res = 0
    cur_node = start
    for c in word:
        if len(cur_node.child)>=2 or (cur_node.end and len(cur_node.child)==1):
            res+=1
        cur_node = cur_node.child[c]
    return res

if __name__=='__main__':
    while True:
        try:
            N = int(input())
        except:
            break
        start = Node(True)
        ans = 0
        word_list=[]
        for _ in range(N):
            word = input().rstrip()
            add(start,word)
            word_list.append(word)
        for word in word_list:
            ans+=find(start,word)
        print(f'{ans/N:.2f}')