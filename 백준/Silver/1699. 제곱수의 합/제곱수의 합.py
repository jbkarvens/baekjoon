def isSquare(n):
    if n==int(n**0.5)**2:
        return True
    return False
def solve_squares(n):
    if isSquare(n):
        return 1
    for i in range(1,int(n**0.5)+1):
        if isSquare(n-i*i):
            return 2
    for i in range(1,int(n**0.5)+1):
        for j in range(1,int((n-i*i)**0.5)+1):
            if isSquare(n-i*i-j*j):
                return 3
    return 4
        
print(solve_squares(int(input())))