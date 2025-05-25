import re


def is_palindrome(text):
    text = text.lower()

    cleaned = re.sub(r'[^a-z0-9]', '', text)

    return cleaned == cleaned[::-1]


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'

print("ОК")