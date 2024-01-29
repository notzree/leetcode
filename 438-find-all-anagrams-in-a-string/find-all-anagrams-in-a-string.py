class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        pfreq, substrfreq = {},{}
        for c in range(len(p)):
            pfreq[p[c]] = pfreq.get(p[c],0)+1
            substrfreq[s[c]] = substrfreq.get(s[c],0)+1
        res = [0] if pfreq == substrfreq else []
        for c in range(len(p),len(s)):
            print(c,c-len(p))
            substrfreq[s[c]] = substrfreq.get(s[c],0)+1
            substrfreq[s[c-len(p)]] -=1
            if substrfreq[s[c-len(p)]] == 0:
                substrfreq.pop(s[c-len(p)])
            if substrfreq == pfreq:
                res.append(c-len(p)+1)
        return res





        
        
        
        