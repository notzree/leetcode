class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for i in strs:
            sortedString = ''.join(sorted(i))
            if sortedString in anagrams:
                anagrams[sortedString].append(i)
            else:
                anagrams[sortedString] = [i]
        return list(anagrams.values())
