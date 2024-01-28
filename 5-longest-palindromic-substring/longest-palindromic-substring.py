class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_l = 0
        res_r =0
        resLen = 0
        for i in range(len(s)):
            #For each element, consider it to be the center of a palindrome. 
            #We first check for odd length palindromes
            l,r = i,i
            while l>=0 and r <len(s) and s[l] == s[r]:
                if (r-l+1)> resLen:
                    
                    res_l=l
                    res_r=r+1
                    resLen = r-l+1
                l-=1
                r+=1
            #Check even length palindromes:
            l,r = i,i+1
            while l>=0 and r <len(s) and s[l]==s[r]:
                if (r-l+1 )> resLen:
                    res_l=l
                    res_r=r+1
                    resLen = r-l+1
                l-=1
                r+=1
        return s[res_l:res_r]
            
                



        