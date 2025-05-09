def multiply_even_sum(pair_list):
    if not pair_list:
        return 0
    even_sum = sum(pair_list[::2])
    result = even_sum * pair_list[-1]
    return result


pair_list = [3, 98, 5, 14, 0, 5]
print(multiply_even_sum(pair_list))