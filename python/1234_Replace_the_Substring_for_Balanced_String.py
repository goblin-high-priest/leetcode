"""
    Algorithm adapted from the solution to LeetCode problem "Replace the Substring for Balanced String",
    as presented in the article:
    https://leetcode.cn/problems/replace-the-substring-for-balanced-string/solutions/2108358/tong-xiang-shuang-zhi-zhen-hua-dong-chua-z7tu/
"""
class Solution:
    def balancedString(self, s: str) -> int:
        m = len(s) // 4
        cnt = Counter(s)

        if len(cnt) == 4 and min(cnt.values()) == m:
            return 0

        res, left = float('inf'), 0

        for right, c in enumerate(s):
            cnt[c] -= 1

            while max(cnt.values()) <= m:
                res = min(res, right - left + 1)
                cnt[s[left]] += 1
                left += 1
            
        return res