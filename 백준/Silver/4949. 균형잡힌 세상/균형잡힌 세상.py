paren=['(',')','[',']']
while True:
    sen=input()
    if len(sen)==1 and sen[0]=='.':
        break
    stack_=[]
    isbalanced=True
    for i in range(len(sen)):
        if sen[i] in paren:
            if sen[i]=='(' or sen[i]=='[':
                stack_.append(sen[i])
            elif len(stack_)==0:
                isbalanced=False
                break
            else:
                tmp=stack_.pop()
                if (tmp=='(' and sen[i]!=')') or (tmp=='[' and sen[i]!=']'):
                    isbalanced=False
                    break
    if len(stack_)!=0:
        isbalanced=False
    if isbalanced:
        print('yes')
    else:
        print('no')