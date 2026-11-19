from collections import defaultdict
from heapq import heapify, heappop, heappush

class MovieRentingSystem:

    def __init__(self, n: int, entries: list[list[int]]):
        self.prices = {}
        self.versions = {}
        self.available = defaultdict(list)
        self.rented = []

        for shop, movie, price in entries:
            self.prices[(shop, movie)] = price
            self.versions[(shop, movie)] = 0

            self.available[movie].append((price, shop, movie, 0))

        for heap in self.available.values():
            heapify(heap)
    
    def top_five(self, heap):
        selected = []

        while heap and len(selected) < 5:
            price, shop, movie, version = heappop(heap)

            if version != self.versions[(shop, movie)]:
                continue
            
            selected.append((price, shop, movie, version))

        for record in selected:
            heappush(heap, record)
        
        return selected

    def search(self, movie: int) -> list[int]:
        
        if movie not in self.available:
            return []
        
        records = self.top_five(self.available[movie])

        return [shop for price, shop, movie, version in records]

    def rent(self, shop: int, movie: int) -> None:
        key = (shop, movie)
        self.versions[key] += 1

        price = self.prices[key]
        version = self.versions[key]

        heappush(self.rented, (price, shop, movie, version))

    def drop(self, shop: int, movie: int) -> None:
        key = (shop, movie)
        self.versions[key] += 1

        price = self.prices[key]
        version = self.versions[key]

        heappush(self.available[movie], (price, shop, movie, version))

    def report(self) -> list[list[int]]:
        records = self.top_five(self.rented)
        return [[shop, movie] for price, shop, movie, version in records]


# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
