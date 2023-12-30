numbers = list(map(float, input().split()))

for num in set(numbers):
    print(f"{num:.1f} - {numbers.count(num)} times")
