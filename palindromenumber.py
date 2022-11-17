class findpalindrome:

    def __init__(self):
        self.inp = int(input("Enter the number: "))

    def palindrome(self):
        if str(self.inp) == str(self.inp)[::-1]:
            print(True)
        else:
            print(False)


if __name__ == '__main__':
    PC = findpalindrome()
    PC.palindrome()
