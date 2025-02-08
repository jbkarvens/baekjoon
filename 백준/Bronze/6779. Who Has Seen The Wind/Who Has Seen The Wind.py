h=int(input())
M=int(input())
done=False
for t in range(1,M+1):
    A=-6*pow(t,4)+h*pow(t,3)+2*t*t+t
    if A<=0:
        print(f'The balloon first touches ground at hour: {t}')
        done=True
        break
if not done:
    print('The balloon does not touch ground in the given time.')
    