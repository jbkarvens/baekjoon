import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
parent=dict()
left_child=dict()
right_child=dict()
for i in range(n):
    a,b,c=input().split()
    left_child[a]=b
    right_child[a]=c
    if b!='.':
        parent[b]=a
    if c!='.':
        parent[c]=a
while a in parent:
    a=parent[a]
root=a

def preorder(root):
    if root=='.':
        return ''
    return root+preorder(left_child[root])+preorder(right_child[root])

def inorder(root):
    if root=='.':
        return ''
    return inorder(left_child[root])+root+inorder(right_child[root])

def postorder(root):
    if root=='.':
        return ''
    return postorder(left_child[root])+postorder(right_child[root])+root

print(preorder(root))
print(inorder(root))
print(postorder(root))