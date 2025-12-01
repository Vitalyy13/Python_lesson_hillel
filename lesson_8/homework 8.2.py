def is_palindrome(text):
    cleaned = ""
    for ch in text:
        if ch.isalnum():
            cleaned += ch.lower()
    reversed_cleaned = cleaned[::-1]
    return cleaned == reversed_cleaned
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
