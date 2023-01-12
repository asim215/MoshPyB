# Even number from 1 to 10
count = 0
for n in range(1, 101):
    if n % 2 == 0:
        print(n)
        count += 1
print(f"We have {count} even numbers")
