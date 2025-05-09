my_list = [57, 42, 0, 87, 0, 1, 'xdd', 0, 333333]

non_zero = []
for x in my_list:
    if x != 0:
        non_zero.append(x)

zero_count = my_list.count(0)
result = non_zero + [0] * zero_count

print(result)