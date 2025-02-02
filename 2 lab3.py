def temp(far):
    res = (5 / 9) * (far - 32)
    return res
far=int(input())
cel=temp(far)
print(cel)