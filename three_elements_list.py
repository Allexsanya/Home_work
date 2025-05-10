import random

my_list = [random.randint(0, 100) for _ in range(random.randint(3, 10))]
new_list = [my_list[0], my_list[2], my_list[-2]]

print("Full list:", my_list)
print("New list:", new_list)

pass