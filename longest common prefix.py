class longestcommonprefix:
    def __init__(self):
        self.strs = ["flower", "flow", "flowight"]
        self.max = 0
        self.min = len(self.strs[0])
        self.result = []

    def findminmax(self):
        for i in range(len(self.strs)):
            if self.max < len(self.strs[i]):
                self.max = len(self.strs[i])
            if self.min > len(self.strs[i]):
                self.min = len(self.strs[i])

    def funlong(self, a):
        count = 0
        for j in range(len(a) - 1):
            if a[j] == a[j + 1]:
                count = count + 1
            if count + 1 == len(a):
                self.result.append(a[j])

    def longg(self):
        for i in range(self.min):
            a = [x[i] for x in self.strs]
            self.funlong(a)

    def output(self):
        print(self.result)

    def Main(self):
        self.findminmax()
        self.longg()
        self.output()


if __name__ == '__main__':
    LCP = longestcommonprefix()
    LCP.Main()
