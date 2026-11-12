class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # shortest str is the common one 
        sorted_strings = sorted(strs, key=lambda x: len(x))
        common_string = sorted_strings[0]

        mini=len(common_string)
        for s in strs:
            length = 0
            for i in range(len(common_string)):
                if s[i] != common_string[i]:
                    mini = min(mini, i)
                    break
        return common_string[:mini] if mini !=0 else ""





