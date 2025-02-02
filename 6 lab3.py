def res():
    sentence=input()
    reversed= ' '.join(sentence.split()[::-1])
    return reversed
print(res())