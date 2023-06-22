import math
def kth(a:list, k:int)->int:
    k-=1
    def select(low,high,k):
        while high>low:
            if high-low>600:
                n=high-low+1
                i=k-low+1
                z=math.log(n)
                s=0.5*math.exp(2*z/3)
                s=int(s)
                if i-n/2>0:
                    sgn=1
                elif i-n/2<0:
                    sgn=-1
                else:
                    sgn=0
                sd=0.5*math.sqrt(z*s*(n-s)/n)*sgn
                newLow = max(low,k-i*s/n+sd)
                newHigh = min(high,k+(n-i)*s/n+sd)
                newLow=int(newLow)
                newHigh=int(newHigh)
                select(newLow,newHigh,k)
            t = a[k]
            i = low
            j = high
            a[low],a[k]=a[k],a[low]
            if a[high]>t:
                a[high],a[low]=a[low],a[high]
            while i<j:
                a[i],a[j]=a[j],a[i]
                i+=1
                j-=1
                while a[i]<t:
                    i+=1
                while a[j]>t:
                    j-=1
            if a[low]==t:
                a[low],a[j]=a[j],a[low]
            else:
                j+=1
                a[j],a[high]=a[high],a[j]
            if j<=k:
                low=j+1
            if k<=j:
                high = j-1
    select(0,len(a)-1,k)
    return a[k]