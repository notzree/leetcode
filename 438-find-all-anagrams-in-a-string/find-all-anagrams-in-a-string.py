class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #iterate thru string p, append to dict like prev q
        #if s[i] == any letter in p,
        #check from i-> i+len(p) if characters match
        #If it does record the index of i in list
        # return list.
        s_length, p_length = len(s), len(p)
        if p_length > s_length:
            return []
        p_count, s_count = {}, {}
        for i in range(p_length):
            p_count[p[i]] = p_count.get(p[i],0)+1
            s_count[s[i]] = s_count.get(s[i],0)+1
        #sliding window initialized
        res = [0] if s_count == p_count else []
        left = 0
        for right in range(p_length, s_length):
            s_count[s[right]] = s_count.get(s[right],0)+1
            s_count[s[left]] -=1

            if s_count[s[left]]==0: #Pop this because if one hashmap has the key with value = 0 in, when comparing the hashmaps might not compare correctly
                s_count.pop(s[left])
            left+=1 #Update left pointer to reflect the current start index
            if s_count == p_count:
                res.append(left)
        return res
            

            

        



                    



