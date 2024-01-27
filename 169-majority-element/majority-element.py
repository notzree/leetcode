class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = Counter(nums)
        maxcount =0
        maxval = -1
        for n in m:
            if m[n] > maxcount:
                maxval = n
            maxcount = max(maxcount, m[n])
        return maxval

