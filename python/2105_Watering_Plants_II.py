class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        alice, bob = capacityA, capacityB
        left, right = 0, len(plants) - 1
        res = 0

        while left < right:
            if alice >= plants[left]:
                alice -= plants[left]
            else:
                alice = capacityA - plants[left]
                res += 1
            left += 1

            if bob >= plants[right]:
                bob -= plants[right]
            else:
                bob = capacityB - plants[right]
                res += 1
            right -= 1

        if left == right:
            if alice < plants[left] and bob < plants[right]:
                res += 1
        
        return res