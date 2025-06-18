class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        def check(comp, num):
            money = 0

            for metal, s, c in zip(comp, stock, cost):
                money += (num * metal - s if num * metal - s > 0 else 0) * c

                if money > budget:
                    return False
            
            return True

        res = 0
        
        for comp in composition:                       
            left, right = 0, min(stock) + budget + 1

            while left < right:
                mid = (left + right) // 2

                if check(comp, mid):
                    left = mid + 1
                else:
                    right = mid
                
            res = max(res, left - 1)
        
        return res
                
            
