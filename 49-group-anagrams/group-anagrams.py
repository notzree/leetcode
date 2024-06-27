class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) ==0:
            return [[""]]
        result = {}
        for s in strs:
            sorted_string = ''.join(sorted(s))
            if sorted_string in result:
                result[sorted_string].append(s)
            else:
                result[sorted_string]=[s]
        return list(result.values())



