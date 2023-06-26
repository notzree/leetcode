class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Sliding window
        #Want substring of max length containing all K's. 
        #Can do at most k replacements
        #Brute force soln?
        #use dict to maintain window
        #keep expanding the window until there are k diff characters from the majority
        maxCount = 0
        maxLength = 0
        i = 0
        w = {}
        for i in range(len(s)):
            w[s[i]] = w.get(s[i],0)+1
            maxCount = max(maxCount, w[s[i]])
            if maxLength-maxCount < k:
                maxLength +=1
            else:
                #The window now has more than K different characters, must remove something... 
                #We remove the character at the start of the subsequence. #This "Slides our window"
                #We don't update the maxCount again here because we want maxCount to only refer to the maxCount of the answer's subsequence, ie: currently after removing the character our maxLength is 1 less than what it actually is. We will update it next itr
                w[s[i-maxLength]] -=1
        return maxLength
        




        # while i - maxCount != k:
        #     print(s[i])
        #     w[s[i]] = w.get(s[i],0)+1
        #     
        #     i = i +1
        # print(maxCount)
        # return -1


                
            
                

