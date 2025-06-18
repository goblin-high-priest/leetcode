class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:

        def check(thres):
            a = nums.copy()

            for i in range(len(nums) - 1, -1, -1):
                x = a[i]

                if x > thres:
                    a[i-1] += x - thres

            return a[0] <= thres

        return bisect_left(range(max(nums)), True, key=check)
