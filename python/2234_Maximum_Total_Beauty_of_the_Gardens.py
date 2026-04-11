class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        n = len(flowers)
        for i in range(n):
            flowers[i] = min(flowers[i], target)
        
        left_flowers = newFlowers - (target * n - sum(flowers))

        if left_flowers == newFlowers:
            return n * full
        
        if left_flowers >= 0:
            return max((target - 1) * partial + (n - 1) * full, n * full)
        
        flowers.sort()

        res = pre_sum = j = 0
        for i in range(1, n + 1):
            left_flowers += target - flowers[i-1]

            if left_flowers < 0:
                continue
            
            while j < i and flowers[j] * j - pre_sum <= left_flowers:
                pre_sum += flowers[j]
                j += 1
            
            avg = (left_flowers + pre_sum) // j
            total_beauty = avg * partial + (n - i) * full
            res = max(res, total_beauty)
        
        return res
