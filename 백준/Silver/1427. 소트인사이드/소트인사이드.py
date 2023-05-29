sen=input()
lst=[int(sen[i]) for i in range(len(sen))]
lst.sort(reverse=True)
for i in range(len(lst)):
    lst[i]=str(lst[i])
print(''.join(lst))