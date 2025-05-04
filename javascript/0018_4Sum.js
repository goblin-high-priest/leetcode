/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
/**
    Algorithm adapted from the solution to LeetCode problem "4Sum",
    as presented in the article:
    https://leetcode.cn/problems/4sum/solutions/2344514/ji-zhi-you-hua-ji-yu-san-shu-zhi-he-de-z-1f0b/
 */
var fourSum = function(nums, target) {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    const ans = [];
    for (let a = 0; a < n - 3; a++) {
        const x = nums[a];
        if (a > 0 && x === nums[a - 1]) continue;
        if (x + nums[a+1] + nums[a+2] + nums[a+3] > target) break;
        if (x + nums[n-3] + nums[n-2] + nums[n-1] < target) continue;
        for (let b = a + 1; b < n - 2; b++) {
            const y = nums[b];
            if (b > a + 1 && y === nums[b-1]) continue;
            if (x + y + nums[b+1] + nums[b+2] > target) break;
            if (x + y + nums[n-2] + nums[n-1] < target) continue;
            let c = b + 1, d = n - 1;
            while (c < d) {
                const s = x + y + nums[c] + nums[d];
                if (s < target) c++;
                else if (s > target) d--;
                else {
                    ans.push([x, y, nums[c], nums[d]]);
                    for (c++; c < d && nums[c] === nums[c-1]; c++);
                    for (d--; c < d && nums[d] === nums[d+1]; d--);
                }
            }
        }
    }
    return ans;
};