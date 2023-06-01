sen=input()
test_sen=input()
m=len(test_sen)
stack=[]
for i in range(len(sen)):
    stack.append(sen[i])
    if ''.join(stack[-m:])==test_sen:
        for _ in range(m):
            stack.pop()
if len(stack)==0:
    print('FRULA')
else:
    print(''.join(stack))