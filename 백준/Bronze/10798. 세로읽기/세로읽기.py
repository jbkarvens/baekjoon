lst=[]
new_lst=[]
for _ in range(5):
    lst.append(input())
for j in range(max([len(sen) for sen in lst])):
    for i in range(5):
        if j<len(lst[i]):
            new_lst.append(lst[i][j])
print(''.join(new_lst))