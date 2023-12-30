cars = int(input())
entries = set()

for _ in range(cars):
    in_out, car_number = input("Enter IN/OUT and car number separated by comma: ").split(',')
    
    if in_out.lower() == "in" and len(car_number) == 8:
        entries.add(car_number)
    elif in_out.lower() == "out":
        print(car_number in entries or "False")
    else:
        print("Invalid in/out")

print("\n".join(entries) or "No entries")
