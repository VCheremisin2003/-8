class cell():
    def __init__(self, number):
        self.number = number
    def __add__(self, other):
        answer = self.number + other.number
        return answer
    def __sub__(self, other):
        if self.number <= other.number:
            print("разность не положительная")
        else:
            answer = self.number - other.number
            return answer
    def __mul__(self, other):
        answer = self.number*other.number
        return answer
    def __floordiv__(self, other):
        answer = self.number//other.number
        answer = cell(answer)
        return
    def make_order(self):
        while self.number>0:
            if self.number-5 > 0:
                print("*"*5)
            else:
                print("*"*(self.number))
            self.number -= 5

cell1 = cell(10)
cell2 = cell(11)
print(cell1 + cell2)
cell3 = cell(cell1+cell2)
cell3.make_order()
