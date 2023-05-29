lst=[]
for _ in range(10):
    lst.append(int(input())%42)
print(len(list(dict.fromkeys(lst))))