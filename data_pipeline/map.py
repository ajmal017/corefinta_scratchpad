# Pseudocode for map.
# def map(func, seq):
#     # Return `Map` object with
#     # the function applied to every
#     # element.
#     return Map(
#         func(x)
#         for x in seq)

values = [1, 2, 3, 4, 5]
add_10 = list(map(lambda x: x + 10, values))
add_20 = list(map(lambda x: x + 20, values))
print(add_10)
print(add_20)
