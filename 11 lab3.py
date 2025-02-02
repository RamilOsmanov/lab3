def is_palindrome(s):
    cleaned_str = ''.join(e for e in s if e.isalnum()).lower()
    return cleaned_str == cleaned_str[::-1]

input_str = input()
if is_palindrome(input_str):
    print("Yes")
else:
    print("No")
