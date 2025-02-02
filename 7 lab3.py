def has33(numbers):
    for i  in range(len(numbers)):
        if numbers[i]==3 and numbers[i+1]== 3 :
            return True
    return False



numbers = list(map(int, input().split()))
print(has33(numbers))