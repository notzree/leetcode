class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # Using Counter to get frequencies
        freq = Counter(nums)

        # Directly building the final sorted list
        return sorted(nums, key=lambda x: (freq[x], -x))  


        