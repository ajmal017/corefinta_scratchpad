
# https://app.dataquest.io/c/48/m/263/functional-programming/2/comparing-object-oriented-to-functional

class LineCounter:
    def __init__(self, filename):
        self.file = open(filename, 'r')
        self.lines = []

    def read(self):
        self.lines = [line for line in self.file]

    def count(self):
        return len(self.lines)

lc = LineCounter('sample3.txt')
print(lc.lines)

print(lc.count())

lc.read()

print(lc.lines)

print(lc.count())

