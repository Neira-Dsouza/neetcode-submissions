class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap={}
        an={}
        if len(s)!=len(t):
            return False
        for ch in s:
            hashmap[ch]=hashmap.get(ch,0)+1
        for ch in t:
            if ch not in hashmap:
                return False
            an[ch]=an.get(ch,0)+1
        for ch in t:
            if hashmap[ch]!=an[ch]:
                return False
        return True
        # return hashmap