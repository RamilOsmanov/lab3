def spy_game(numbers):
    for i in range(len(numbers) - 2):
        if numbers[i] == 0 and numbers[i + 1] == 0 and numbers[i + 2] == 7:
            return True
    return False


numbers = list(map(int, input().split()))
print(spy_game(numbers)) 
