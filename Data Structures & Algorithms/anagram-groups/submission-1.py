class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        chars={}
        for i in strs:
            key=''.join(sorted(i))
            if key not in chars:
                chars[key]=[]
            chars[key].append(i)
        return list(chars.values())