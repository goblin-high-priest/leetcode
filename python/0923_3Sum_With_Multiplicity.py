class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr.sort()
        res = 0

        for i in range(len(arr) - 2):
            tar = target - arr[i]
            l, r = i + 1, len(arr) - 1

            while l < r:

                if arr[l] + arr[r] < tar:
                    l += 1
                elif arr[l] + arr[r] > tar:
                    r -= 1
                else:
                    l_tmp, r_tmp = arr[l], arr[r]
                    
                    if l_tmp != r_tmp:
                        l_cnt, r_cnt = 0, 0

                        while l < r and arr[l] == l_tmp:
                            l += 1
                            l_cnt += 1
                        
                        while l <= r and arr[r] == r_tmp:
                            r -= 1
                            r_cnt += 1
                        
                        res += l_cnt * r_cnt
                    else:
                        cnt = r - l + 1
                        res += cnt * (cnt - 1) // 2
                        break
                
        return res % (10 ** 9 + 7)