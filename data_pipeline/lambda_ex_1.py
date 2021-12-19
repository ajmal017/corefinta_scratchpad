# https://www.w3resource.com/python-exercises/lambda/index.php

# 1. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
# also create a lambda function that multiplies argument x with argument y and print the result. Go to the editor

# r = lambda a : a + 15
# print(r(10))
#
# r = lambda x, y : x * y
# print(r(12, 4))
#
# def func_compute(n):
#     return lambda x : x * n
#
# double_result = func_compute(2)
# print("Double the number of 15 =", double_result(15))
# triple_result = func_compute(3)
# print("Triple the number of 15 =", triple_result(15))
# quad_result = func_compute(4)
# print("Quadruple the number of 15 =", quad_result(15))
# quint_result = func_compute(5)
# print("Quintuple the number 15 =", quint_result(15))
#
# unsorted = [('English', 88), ('Science', 90), ('Math', 97), ('Social Sciences', 82)]

# Sort on the second tuple value (the integer).
#print(sorted(unsorted, key=lambda x: x[0]))

# subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# print("Original list of tuples:")
# print(subject_marks)
# subject_marks.sort(key = lambda x: x[1])
# print("\nSorting the List of Tuples:")
# print(subject_marks)

# unsorted.sort(key=lambda x: x[1])
# print(unsorted)

# orig_dict = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
# print(f'Original list of dictionaries: \n{orig_dict}')
# # sorted_dict = sorted(orig_dict, key=lambda x: x['color'])
# # print(f'Sorted list of dictionaries: \n{sorted_dict}')
#
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print("Original list of integers:")
# print(nums)
# print("\nEven numbers from the said list:")
# even_nums = list(filter(lambda x: x%2 == 0, nums))
# print(even_nums)
# print("\nOdd numbers from the said list:")
# odd_nums = list(filter(lambda x: x%2 != 0, nums))
# print(odd_nums)
#
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print("Original list of integers:")
# print(nums)
# print("\nSquare every number from the said list:")
# square_nums = list(map(lambda x: x**2, nums))
# print(square_nums)
# print("\nCube numbers from the said list:")
# cube_nums = list(map(lambda x: x**3, nums))
# print(cube_nums)
#
# starts_with = lambda x: True if x.startswith('P') else False
# print(starts_with('Python'))
# starts_with = lambda x: True if x.startswith('P') else False
# print(starts_with('Java'))
#
# import datetime
# now = datetime.datetime.now()
# print(now)
# year = lambda x: x.year
# month = lambda x: x.month
# day = lambda x: x.day
# t = lambda x: x.time()
# print(year(now))
# print(month(now))
# print(day(now))
# print(t(now))
#
# def num_there(s):
#     return any(i.isdigit() for i in s)
#
# king = 'i shall have 3 cakes'
# print(num_there(king))
# servant = 'i do not have any cakes'
# print(num_there(servant))

is_num = lambda q: q.replace('.','',1).isdigit()
# print(is_num('26587'))
# print(is_num('4.2365'))
# print(is_num('-12547'))
# print(is_num('00'))
# print(is_num('A001'))
# print(is_num('001'))

is_num1 = lambda r: is_num(r[1:]) if r[0]=='-' else is_num(r)
print(is_num1('bro'))
print(is_num1('-24587.11'))
print(is_num1('26587'))
print(is_num1('4.2365'))
print(is_num1('-12547'))
print(is_num1('00'))
print(is_num1('A001'))
print(is_num1('001'))
