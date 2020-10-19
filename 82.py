class MyOwnError():
    def __init__(self, number_1):
        self.number_1 = number_1
    def __floordiv__(self, other):
        if other.number_1 != 0:
            return self.number_1//other.number_1
        else:
            print("error")

num1 = MyOwnError(2)
num2 = MyOwnError(0)
num1//num2
