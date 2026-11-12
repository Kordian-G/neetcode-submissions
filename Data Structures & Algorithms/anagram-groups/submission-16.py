class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        checked = {}
        for i in range(len(strs)):
            key = str(sorted(strs[i]))
            if key not in checked:
                checked[key] = []
            checked[key].append(strs[i])
        return list(checked.values())            