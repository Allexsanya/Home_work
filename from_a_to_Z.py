import string

all_letters = string.ascii_letters

user_input = input("Enter two letters with defis, like a-c: ")

start, end = user_input.split('-')

start_index = all_letters.index(start)
end_index = all_letters.index(end)

result = all_letters[start_index:end_index + 1]

print(result)