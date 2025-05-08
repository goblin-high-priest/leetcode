class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int i = 0, j = 0, sum = 0;
        int result = Integer.MAX_VALUE;
        for (;j < nums.length; j++) {
            sum += nums[j];
            while (sum >= target) {
                result = Math.min(result, j - i + 1);
                sum -= nums[i++];
            }
        }
        return result == Integer.MAX_VALUE ? 0 : result;
    }
}