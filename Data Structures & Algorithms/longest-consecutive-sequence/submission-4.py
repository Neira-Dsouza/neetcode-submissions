class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        sets=sorted(set(nums))
        if len(sets)==0:
            return 0
        count=1
        final=1
        for i in range(len(sets)-1):
            if sets[i+1]==(sets[i]+1):
                count+=1
            else:
                count=1
            final=max(final,count)
        return final
        # return sets