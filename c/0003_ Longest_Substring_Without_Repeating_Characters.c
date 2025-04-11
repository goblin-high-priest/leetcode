int lengthOfLongestSubstring(char* s) {
    int n = strlen(s), ans = 0, i = 0;
    int mp[128]; // 假设ASCII字符集，128足够了
    memset(mp, -1, sizeof(mp)); // 使用-1初始化数组，表示字符尚未出现

    for (int j = 0; j < n; j++) {
        if (mp[s[j]] != -1) {
            i = i > mp[s[j]] ? i : mp[s[j]]; // 更新i为当前字符上一次出现位置的下一个位置
        }
        ans = ans > (j - i + 1) ? ans : (j - i + 1); // 更新ans为当前最长的无重复字符子串的长度
        mp[s[j]] = j + 1; // 更新当前字符的最后出现位置
    }
    return ans;
}