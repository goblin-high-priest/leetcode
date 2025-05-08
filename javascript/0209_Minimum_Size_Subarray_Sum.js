/**
 * @param {number} target
 * @param {number[]} nums
 * @return {number}
 */
var minSubArrayLen = function(target, nums) {
    const length = nums.length;
    let left = 0;
    let sum = 0;
    let res = length + 1;

    for (let right = 0; right < length; right++) {
        sum += nums[right];
        while (sum >= target) {
            res = Math.min(right - left + 1, res);
            sum -= nums[left];
            left++;
        }
    }

    return res == length + 1 ? 0 : res;
};