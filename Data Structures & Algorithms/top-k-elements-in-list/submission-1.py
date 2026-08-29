class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        lists=[]
        sorted_l=[]
        for i in nums:
            hashmap[i]=hashmap.get(i,0)+1
        for i in hashmap:
            lists.append([hashmap[i],i])
        lists.sort()
        final=[]
        for i in range(k):
            final.append(lists[len(lists)-i-1][1])
        return final