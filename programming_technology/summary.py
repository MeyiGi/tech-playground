def summary(numbers):
    if len(numbers) == 0:
        return None

    total = sum(numbers)
    count = len(numbers)
    average = total / count

    return total, count, average


numbers = [10, 20, 30, 40, 50]

result = summary(numbers)
print(result)

sayi = 4 
print(f"{10 / 4:.2f}")