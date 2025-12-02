class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        f = [0] * n
        f[0] = nums[0]
        q = deque([0])

        for i in range(1, n):

            if q[0] < i - k:
                q.popleft()
            
            f[i] = f[q[0]] + nums[i]

            while q and f[i] >= f[q[-1]]:
                q.pop()
            
            q.append(i)

        return f[-1]
