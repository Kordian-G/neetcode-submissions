class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        values = {}
        for i in range(len(strs)):
            key_i = str(sorted(strs[i]))
            if key_i not in values.keys():
                values[key_i] = []
            values[key_i].append(strs[i])
        return list(values.values())
            





        