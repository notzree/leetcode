class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #iterate thru string p, append to dict like prev q
        #if s[i] == any letter in p,
        #check from i-> i+len(p) if characters match
        #If it does record the index of i in list
        # return list.
        d = {}
        index = []
        
        p_length = len(p)
        s_length = len(s)
        if p_length > s_length:
            return index
        for i in p:
            d[i] = d.get(i,0) + 1
        #Dictionary is now {char:count} of p
        #Full pass on window of len(p)
        for i in range(p_length-1):
            if s[i] in d: 
                d[s[i]] -=1
        #Start @ -1 for convenience (see that one comment)
        for i in range(-1,s_length - p_length + 1):
            if i > -1 and s[i] in d:
                d[s[i]] +=1
            if i + p_length < s_length and s[i+ p_length] in d:
                d[s[i+p_length]] -=1
            if not any(d.values()):
                index.append(i+1)
              
                
        return index

                    



