class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        pos_lists = defaultdict(list)

        for i, x in enumerate(nums):
            pos_lists[x].append(i)

        res = 0

        for pos in pos_lists.values():

            if len(pos) <= res:
                continue
            
            left = 0

            for right in range(len(pos)):
                
                while pos[right] - pos[left] - (right - left) > k:
                    left += 1

                res = max(res, right - left + 1)
            
        return res