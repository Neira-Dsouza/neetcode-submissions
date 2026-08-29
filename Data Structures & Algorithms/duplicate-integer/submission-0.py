class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap={}
        for i in nums:
            if i in hashmap:
                return True
            hashmap[i]=hashmap.get(i,0)+1
        return False
        