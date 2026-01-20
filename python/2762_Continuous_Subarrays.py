class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        min_q = deque()
        max_q = deque()
        res = left = 0

        for right, x in enumerate(nums):
            
            while min_q and x <= nums[min_q[-1]]:
                min_q.pop()
            min_q.append(right)

            while max_q and x >= nums[max_q[-1]]:
                max_q.pop()
            max_q.append(right)
        
            while nums[max_q[0]] - nums[min_q[0]] > 2:
                left += 1

                if min_q[0] < left:
                    min_q.popleft()
                
                if max_q[0] < left:
                    max_q.popleft()
                
            res += right - left + 1
        
        return res