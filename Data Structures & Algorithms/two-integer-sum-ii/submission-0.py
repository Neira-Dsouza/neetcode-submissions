class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index={}
        for i in range(len(numbers)):
            find=target-numbers[i]
            if find in index:
                return [index[find],i+1]
            index[numbers[i]]=i+1
            # return [index[find],i+1]