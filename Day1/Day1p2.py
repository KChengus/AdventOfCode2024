import re

class Solution():
    def __init__(self):
        self.content = list()

    def solve(self):
        left, right = [], {}
        for line in self.content:
            left.append(int(line[0]))
            r = int(line[1])
            if r not in right:
                right[r] = 0
            right[r] += 1

        ret = 0
        for num in left:
            if num in right:
                ret += num * right[num]
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