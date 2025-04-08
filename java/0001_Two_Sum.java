import java.util.stream.IntStream;
class Solution {
    public int[] twoSum(int[] nums, int target) {
        // int[] list = new int[2];
        // for (int i = 0; i < nums.length-1; i++) {
        //     int n = nums[i];
        //     for (int j = i + 1; j < nums.length; j++) {
        //         int m = nums[j];
        //         if (n + m == target) {
        //             list[0] = i;
        //             list[1] = j;
        //             return list;
        //         }

        //     }
        // }
        // return list;
        int[] res = new int[2];
        int[] temp = new int[nums.length];

        System.arraycopy(nums, 0, temp, 0, nums.length);
        Arrays.sort(nums);
        for (int i = 0, j = nums.length - 1; i < j;) {
            if (nums[i] + nums[j] < target) {
                i++;
            } else if (nums[i] + nums[j] > target) {
                j--;
            } else {
                final int num1 = nums[i];
                final int num2 = nums[j];
                int index1 = IntStream.range(0, temp.length).filter(x -> temp[x] == num1).findFirst().orElse(-1);
                int index2 = IntStream.range(0, temp.length).filter(x -> temp[x] == num2 && x != index1).findFirst().orElse(-1);
                res[0] = index1;
                res[1] = index2;
                return res;
            }
        }
        return null;
    }
    
}