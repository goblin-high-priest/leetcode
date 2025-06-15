class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        positions = defaultdict(list)

        for i, x in enumerate(arr):
            positions[x].append(i)
        
        self.positions = positions

    def query(self, left: int, right: int, value: int) -> int:
        indices = self.positions[value]

        return bisect_right(indices, right) - bisect_left(indices, left)


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)