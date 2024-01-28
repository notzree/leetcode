class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #iterate thru string p, append to dict like prev q
        #if s[i] == any letter in p,
        #check from i-> i+len(p) if characters match
        #If it does record the index of i in list
        # return list.
        if len(p) > len(s):
            return []
        result = []
        p = ''.join(sorted(p)) 
        for i in range(len(s)-len(p)+1):
            print(i)
            anagram = ''.join(sorted(s[i:i+len(p)]))
            if anagram == p:
                result.append(i)
        return result


                    



