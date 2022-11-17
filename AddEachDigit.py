class sumofeachdigit:
    def __init__(self):
        self.Num = input("Enter the number: ")

    def sumofdigit(self, temp):
        summ = 0
        for num in temp:
            summ = summ + int(num)
        return str(summ)

    def looping(self):
        while len(self.Num) > 1:
            self.Num = self.sumofdigit(self.Num)
        else:
            print("Result =", self.Num)
    def validate(self):
        if int(self.Num) < 0:
            print("The given number is Negative")
            exit()

    def Main(self):
        self.validate()
        self.looping()


if __name__ == '__main__':
    KF = sumofeachdigit()
    KF.Main()

