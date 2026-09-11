# 14. Longest Common Prefix
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort(key=len)

        prefix = ""

        for i in range(len(strs[0])):
            prefix = strs[0][:i + 1]

            for j in range(1, len(strs)):
                if not strs[j].startswith(prefix):
                    return prefix[:-1]

        return prefix
    
# Best, but difficult to understand
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        shortest = min(strs, key=len)

        for i, char in enumerate(shortest):
            for string in strs:
                if string[i] != char:
                    return shortest[:i]

        return shortest