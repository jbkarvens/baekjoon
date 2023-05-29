S,lst=input(),[-1]*26
for i in range(len(S)):
    idx=ord(S[i])-ord('a')
    if lst[idx]==-1:
        lst[idx]=i
print(*lst)