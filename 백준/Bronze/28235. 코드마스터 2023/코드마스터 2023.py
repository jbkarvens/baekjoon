import sys
input=sys.stdin.readline

if __name__=='__main__':
    s=input().rstrip()
    r=''
    if s=='SONGDO':
        r='HIGHSCHOOL'
    elif s=='CODE':
        r='MASTER'
    elif s=='2023':
        r='0611'
    elif s=='ALGORITHM':
        r='CONTEST'
    print(r)