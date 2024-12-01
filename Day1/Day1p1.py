import re

class Solution():
    def __init__(self):
        self.content = list()

    def solve(self):
        left, right = [], []
        for line in self.content:
            left.append(int(line[0]))
            right.append(int(line[1]))
        left.sort()
        right.sort()
        ret = 0
        for i, j in zip(left, right):
            ret += abs(i - j)
        return ret

    def handle_input(self):
        with open('input.txt', 'r') as f:
            for line in f:
                self.content.append(line.split())
                
    def run(self):
        self.handle_input()
        return self.solve()
       

if __name__ == "__main__":
    sol = Solution()
    print(sol.run())