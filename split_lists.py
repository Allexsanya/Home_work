def split_list(spisok):
    length = len(spisok)
    mid = (length + 1) // 2
    return [spisok[:mid], spisok[mid:]]
examples = [[22, 34, 43, 12, 3, 9], [44, 54, 22], [2, 12, 11, 90, 44], [1], [0]]
for example in examples:
    print(f"{example} => {split_list(example)}")
pass
