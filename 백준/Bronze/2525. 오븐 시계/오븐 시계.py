h,m=map(int,input().split())
c=int(input())
t=(h*60+m+c)%1440
print((t//60) if (t>=0) else (t//60+24),t%60)