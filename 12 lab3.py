def histogram(numbers):
    for num in numbers:
        print('*' * num)

numbers = list(map(int, input().split()))
histogram(numbers)
