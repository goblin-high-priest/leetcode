class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions.sort()

        for spell in spells:
            target = success / spell
            res.append(len(potions) - bisect_left(potions, target))

        return res