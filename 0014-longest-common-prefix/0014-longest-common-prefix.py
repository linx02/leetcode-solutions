class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        get shortest string in array
        iterate, looking if char exist in all arrays:
            if exists:
                add to prefix string
                continue iteration,
            if not:
                add to prefix list if not empty
                start again at next index
        """

        shortest_string = min(strs, key=len)
        strs.remove(shortest_string)

        possible_prefixes = []
        prefix = ''
        for i in range(len(shortest_string)):
            prefix += shortest_string[i]
            possible_prefixes.append(prefix)
        
        matches = []
        for prefix in possible_prefixes:
            match = []
            for string in strs:
                if prefix == string[:len(prefix)]:
                    match.append(prefix)
            if len(match) == len(strs):
                matches.append(prefix)

        if len(matches) > 0:
            return max(matches, key=len)
        else:
            return ''