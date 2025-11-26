class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = [0] * (len(nums) - k + 1)
        q = deque()

        for i, x in enumerate(nums):

            while q and x >= nums[q[-1]]:
                q.pop()
            
            q.append(i)

            if i - q[0] + 1 > k:
                q.popleft()
            
            if i >= k - 1:
                res[i-k+1] = nums[q[0]]
            
        return res