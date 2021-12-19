class LineCounter:
    def __init__(self, filename):
        self.file = open(filename, 'r')
        self.lines = []

    def read(self):
        self.lines = [line for line in self.file]

    def count(self):
        return len(self.lines)

lc = LineCounter('example_log.txt')

lc.read()

example_lines = lc.lines

lines_count = lc.count()
