class Solution {
    private int dfs(int i, int[] nums, Integer[] memo) {
            
        if (i < 0) return 0;

        if (memo[i] != null) return memo[i];

        memo[i] = Math.max(dfs(i - 1, nums, memo), dfs(i - 2, nums, memo) + nums[i]);

        return memo[i];
    }
    public int rob(int[] nums) {
        Integer[] memo = new Integer[nums.length];
        return dfs(nums.length - 1, nums, memo);
    }
}