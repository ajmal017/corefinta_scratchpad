def read(filename):
    with open(filename, 'r') as f:
        return [line for line in f]

lines = read('example_log.txt')
# print(lines)

sorted_lines = sorted(lines, key=lambda x: x.split(' ')[5])
print(sorted_lines)


