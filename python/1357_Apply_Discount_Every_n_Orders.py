class Cashier:

    def __init__(self, n: int, discount: int, products: list[int], prices: list[int]):
        self.n = n
        self.discount = discount

        self.count = 0
        self.prices = {}

        for i in range(len(products)):
            self.prices[products[i]] = prices[i]
        
    def getBill(self, product: list[int], amount: list[int]) -> float:
        self.count += 1
        total = 0

        for i in range(len(product)):
            price = self.prices[product[i]]
            total += price * amount[i]

        if self.count % self.n == 0:
            total = total * (100 - self.discount) / 100
        
        return float(total)


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
