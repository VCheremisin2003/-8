class size():
    def __init__(self, param):
        self.param = param
    @property
    def costum(self):
        print(2 * self.param + 0.3)

    @property
    def suit(self):
        print(self.param/6.5 + 0.5)

f = size(50)
f.costum
f.suit
