class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        hmap = {}
        t_length = len(t)
        max_length = float("infinity")
        start,end=0,0
        for c in t: #init hashmap
            hmap[c] = hmap.get(c,0)+1

        for (i,c) in enumerate(s):
            if c in hmap:
                hmap[c] = hmap[c]-1
                if hmap[c] >=0: #greater equal to zero
                    t_length -=1
            while t_length ==0:
                if i-left+1 < max_length:
                    max_length = i-left+1
                    start=left
                    end = i
                if s[left] in hmap:
                    hmap[s[left]] +=1
                    if hmap[s[left]] >0:
                        #we are missing hmap[left]
                        t_length +=1
                left+=1
        return s[start:end+1] if max_length != float("infinity") else ""





            
        
        
        