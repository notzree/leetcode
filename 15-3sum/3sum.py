class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # unique groupings of unique numbers that sum to 0
        # Idea: split up the input into negatives, positives, and zeros
        result = set()
        n,p,z = [], [], []
        
        for num in nums:
            if num > 0:
                p.append(num)
            elif num == 0:
                z.append(num)
            else:
                n.append(num)
        N,P = set(n), set(p)
        if z:
            for num in P:
                if -1*num in N:
                    result.add((-1*num, 0, num))
        if len(z) >=3:
            result.add((0,0,0))
        
        #do 2sum
        for i in range(len(n)):
            for j in range(i+1, len(n)):
                target = -1*(n[i]+n[j])
                if target in P:
                    result.add(tuple(sorted([n[i],n[j],target])))

        for i in range(len(p)):
            for j in range(i+1, len(p)):
                target = -1*(p[i]+p[j])
                if target in N:
                    result.add(tuple(sorted([p[i],p[j],target])))
        return result
        
        
            













                




        
        