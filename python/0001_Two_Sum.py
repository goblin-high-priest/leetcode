class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # list = []
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+nums[j] == target:

        #             return [i, j]
        mapping = {}
        for i in range(len(nums)):
            if target - nums[i] in mapping:
                return [mapping[target - nums[i]], i]
            mapping[nums[i]] = i