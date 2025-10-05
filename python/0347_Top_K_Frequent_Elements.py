class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter()
        freq = [[] for _ in range(len(nums) + 1)]
        res = []
        
        for num in nums:
            count[num] = count[num] + 1
        
        for n, c in count.items():
            freq[c].append(n)
        
        for i in range(len(freq) - 1, 0, -1):
            
            for num in freq[i]:
                res.append(num)

                if len(res) == k:
                    return res
