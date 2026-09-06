class MinStack:

    def __init__(self):
        self.store = []
        

    def push(self, val: int) -> None:
        self.store.append(val)

    def pop(self) -> None:
        self.store.pop()

    def top(self) -> int:
        if self.store:
            return self.store[-1]

    def getMin(self) -> int:
        return min(self.store)
