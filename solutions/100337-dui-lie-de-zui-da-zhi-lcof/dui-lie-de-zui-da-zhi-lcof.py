# English description is not available for the problem. Please switch to Chinese.


from collections import deque


class MaxQueue:

    def __init__(self):
        self.queue = deque()

    def max_value(self) -> int:
        if not self.queue:
            return -1
        return max(self.queue)


    def push_back(self, value: int) -> None:
        self.queue.append(value)


    def pop_front(self) -> int:
        if not self.queue:
            return -1
        return self.queue.popleft()



# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
