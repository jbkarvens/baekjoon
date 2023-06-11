import sys
input_func=sys.stdin.readline

cout = [0]
board = {}

def show():
    n=len(board)//4
    show=''
    for i in range(-3,2*n+1):
        if board[i]==None:
            show+='.'
        else:
            show+=str(board[i])
    print(show)
    print(cout[0])

def move(x,y):
    cout[0]+=1
    if board[x]==None or board[x+1]==None or board[y]!=None or board[y+1]!=None:
        print(f'Invalid move:({x},{y})')
        show()
        return
    print(f'{x} to {y}')
    board[x],board[x+1],board[y],board[y+1]=None,None,board[x],board[x+1]

def makeboard(n):
    for i in range(-2*n+1,2*n+1):
        board[i]=None
    for i in range(1,2*n+1):
        board[i]=i%2
    return

def solve(n):
    makeboard(n)
    if n%4==0 or n%4==1:
        i=2*n-2
        j=-1
        while j<i-5:
            move(i,j)
            j+=4
            move(j,i)
            i-=4
        if n%4==0:
            i,j=0,n-1
            while j<2*n-4:
                move(i,j)
                j+=4
                move(j,i)
                i+=4
        elif n%4==1:
            move(n+1,n-2)
            i,j=0,n+1
            move(0,n+1)
            i,j=n+4,0
            while i<2*n-4:
                move(i,j)
                j+=4
                move(j,i)
                i+=4
            move(2*n-1,n-5)
    elif n%4==2:
        if n==6:
            move(10,-1)
            move(7,10)
            move(2,7)
            move(6,2)
            move(0,6)
            move(11,0)
        else:
            move(2*n-2,-1)
            i,j=3,2*n-2
            while i<n-4:
                move(i,j)
                j-=4
                move(j,i)
                i+=4
        
            move(n+1,n+4)
            move(n-4,n+1)
            move(n,n-4)
            move(4,n)
            move(n+5,4)
            
            i,j=n-6,n+5
            while i>5:
                move(i,j)
                j+=4
                move(j,i)
                i-=4
            move(0,2*n-5)
            move(2*n-1,0)
    else:
        if n==3:
            move(2,-1)
            move(5,2)
            move(3,-3)
        else:
            i,j=2*n-2,-1
            while i>n+5:
                move(i,j)
                j+=4
                move(j,i)
                i-=4
            move(n+1,n-8)
            move(n-2,n+1)
            move(n+5,n-2)
            move(n-4,n+5)
            move(n+2,n-4)
            i,j=n-7,n+2
            while i>=0:
                move(i,j)
                j+=4
                move(j,i)
                i-=4
    # show()

if __name__=="__main__":
    cout = [0]
    board = {}
    solve(int(input_func()))