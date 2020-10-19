class matrix():
    def __init__(self, mtrx):
        self.mtrx = mtrx
    def __str__(self):
        b = ""
        for item in self.mtrx:
            k = ""
            for thing in item:
                k += str(thing) + " "
            b += k
            b += '\n'
        return b
    def __add__(self, other):
        k = 0
        m = []
        for item in self.mtrx:
            b = 0
            e = []
            for thing in item:
                d = other.mtrx[k]
                c = d[b] + thing
                e.append(c)
                b+=1
            k+=1
            m.append(e)
            
        m = matrix(m)
        return m

matrix1 = [[1, 2], [3, 4], [5, 6]]
matrix2 = [[1, 2], [3, 4], [5, 6]]

w = matrix(matrix1)
q = matrix(matrix2)
    #def __add__(self.matrix1, self.matrix2):
a = matrix(matrix1)
m = w + q
#r = matrix(m)
print(m)
print(w)