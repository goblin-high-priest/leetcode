class Solution {
    public int trap(int[] height) {
        int left = 0;
        int right = height.length - 1;
        int prefix_max = 0;
        int suffix_max = 0;
        int sum = 0;
        
        while (left <= right) {
            prefix_max = Math.max(prefix_max, height[left]);
            suffix_max = Math.max(suffix_max, height[right]);

            if (prefix_max < suffix_max) {
                sum += prefix_max - height[left];
                left++;
            } else {
                sum += suffix_max - height[right];
                right--;
            }
        }

        return sum;
    }
}