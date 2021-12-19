# Using `def` (old way).
def old_add(a, b):
    return a + b

# Using `lambda` (new way).
new_add = lambda a, b: a + b

print(old_add(2,3))
print(new_add(4,5))

print(old_add(10, 5) == new_add(10, 5))

unsorted = [('b', 6), ('a', 10), ('d', 0), ('c', 4)]

# Sort on the second tuple value (the integer).
print(sorted(unsorted, key=lambda x: x[1]))

