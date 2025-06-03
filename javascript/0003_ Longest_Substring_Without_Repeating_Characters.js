/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(s) {
    const length = s.length;
    const cnt = new Map();
    let left = 0;
    let res = 0;
    
    for (let right = 0; right < length; right++) {
        const c = s[right];
        cnt.set(c, (cnt.get(c) ?? 0) + 1);
        
        while (cnt.get(c) > 1) {
            const c_ = s[left];
            cnt.set(c_, cnt.get(c_) - 1);
            left++;
        }

        res = Math.max(res, right - left + 1);
    }
    
    return res;
};