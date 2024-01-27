class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        m = {}
        for n in nums:
            m[n] = m.get(n,0)+1
        result = list(m.items())
        #Either sort by frequency or by inverse of value (decreasing order)
        result.sort(key = lambda x : (x[1],-x[0]))
        result2 = []
        for v,c in result:
            result2 +=[v]*c     
        return result2        


        