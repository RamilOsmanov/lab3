def uni(numbers):
    result = []
    for num in numbers:
        if num not in result:
            result.append(num) 
    return result

numbers = list(map(int, input().split()))
print(uni(numbers)) 
