import sys
n=int(sys.stdin.readline())
peop_lst=dict()
for _ in range(n):
    name_,status_=sys.stdin.readline().split()
    if status_=='enter':
        peop_lst[name_]=status_
    elif status_ == 'leave':
        del peop_lst[name_]
peop_lst=sorted(peop_lst,reverse=True)
for name_ in peop_lst:
    print(name_)