def read(filename):
    with open(filename, 'r') as f:
        return [line for line in f]

lines = read('example_log.txt')
# print(lines)

ip_addresses = list(map(lambda x: x.split()[0], lines)) # splits line on spaces and then returns first element on split line
print(ip_addresses)
