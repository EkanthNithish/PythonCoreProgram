class twosumleetcode:
    def __init__(self):
        self.n = int(input("Number of Elements in the list: "))
        self.lst = []
        for num in range(self.n):
            temp = int(input())
            self.lst.append(temp)
        self.target = int(input("Enter the target: "))

    def twosum(self):
        for num in range(self.n):
            for num1 in range(num+1,self.n):
                if self.target == self.lst[num] + self.lst[num1]:
                    print([num,num1])

    def Main(self):
        self.twosum()

if __name__ =='__main__':
    obj = twosumleetcode()
    obj.Main()
