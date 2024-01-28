class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        maxLength = 0
        maxCount = 1
        l =0
        #sliding window
        for r in range(len(s)):
            window[s[r]] = window.get(s[r],0)+1
            maxCount=max(maxCount,window[s[r]]) #We only need to update this when we move the right pointer because when moving left, the maxCount would only shrink. Since our condition is length - maxcount <=k, we want both length and maxcount to be maximized to give us the largest size while still remaining <=k
            while (r-l+1-maxCount) > k: #If our window requires more than k replacements, then we need to shrink it until it requires max k replacements.
                    window[s[l]] -=1 #make sure to decrement the counts
                    l+=1
            maxLength = max(maxLength, r-l+1) #We only recalculate the maxLength after we have adjusted the window to fit our requirement. 
        return maxLength

            
                


            

            


        
        



                
            
                

