NUM=835454957
dp_dict={}
def isPalindrome(s):
    for i in range(len(s)//2):
        if s[i]!=s[-1-i]:
            return False
    return True
def dp(lst,sen,end,K):
    if K<=-2:
        return 0
    elif K==-1 and isPalindrome(sen):
        return 1
    if (sen,end,K) in dp_dict:
        return dp_dict[sen,end,K]
    ans=0
    if isPalindrome(sen):
        ans+=1
    r=len(sen)
    if end==False:
        for s in lst:
            r2=len(s)
            if r>r2 and sen[:r2]==s:
                ans+=dp(lst,sen[r2:],False,K-r2-1)
            elif r==r2 and sen==s:
                ans+=dp(lst,'',False,K-r2-1)
            elif r2>r and sen==s[:r]:
                ans+=dp(lst,s[r:][::-1],True,K-r2-1)
    else:
        for s in lst:
            r2=len(s)
            if r>r2 and sen[-r2:]==s:
                ans+=dp(lst,sen[:-r2],True,K-r2-1)
            elif r==r2 and sen==s:
                ans+=dp(lst,'',False,K-r2-1)
            elif r2>r and sen==s[-r:]:
                ans+=dp(lst,s[:-r][::-1],False,K-r2-1)
    ans%=NUM
    dp_dict[sen,end,K]=ans
    return ans
    
    
    
if __name__=='__main__':
    N,K=map(int,input().split())
    lst=[]
    for _ in range(N):
        lst.append(input().rstrip())
    print((dp(lst,'',False,K)-1)%NUM)