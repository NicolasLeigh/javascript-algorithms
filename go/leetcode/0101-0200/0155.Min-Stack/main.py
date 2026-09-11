class MinStack:

    def __init__(self):
        self.s1 = []  # 主栈
        self.s2 = []  # 最小值栈

    def push(self, x: int) -> None:
        self.s1.append(x)

        if not self.s2 or x <= self.getMin():
            self.s2.append(x)

    def pop(self) -> None:
        if self.top() == self.getMin():
            self.s2.pop()

        self.s1.pop()

    def top(self) -> int:
        return self.s1[-1]

    def getMin(self) -> int:
        return self.s2[-1]