class КомплексноеЧисло():
    def __init__(self, first, second):
        self.first = first
        self.second = second



    def __add__(self, other):
        part1 = self.first + other.first
        part2 = self.second + other.second
        return f'{part1} + {part2}i'

    def __sub__(self, other):
        part1 = self.first - other.first
        part2 = self.second - other.second
        return f'{part1} + {part2}i'


a = КомплексноеЧисло(1, 3)
в = КомплексноеЧисло(3, 5)
print(a + в)
print(a - в)