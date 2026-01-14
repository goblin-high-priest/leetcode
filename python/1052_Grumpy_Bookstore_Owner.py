class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        cur_window = tmp = cur = left = 0
        
        for right, x in enumerate(customers):

            if not grumpy[right]:
                cur += x

            if right < minutes:
                if grumpy[right]:
                    cur_window += x
                    tmp = cur_window
                continue
            else:

                if grumpy[right]:
                    tmp += x
                left = right - minutes

                if grumpy[left]: tmp -= customers[left]

                cur_window = max(cur_window, tmp)

        return cur + cur_window