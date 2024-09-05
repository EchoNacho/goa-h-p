# 3) For loop to print numbers from 126 to 0 with different steps
print("Decrement by 1:")
for i in range(126, -1, -1):
    print(i)

print("\nDecrement by 2:")
for i in range(126, -1, -2):
    print(i)

print("\nDecrement by 3:")
for i in range(126, -1, -3):
    print(i)

# 4) For loop to calculate the sum and product of numbers from 1 to 47
print("\nSum using addition (+):")
total_sum = 0
for i in range(1, 48):
    total_sum += i
print(total_sum)

print("\nProduct using multiplication (*):")
product = 1
for i in range(1, 48):
    product *= i
print(product)

# 5) While loop to count down from 100 to 1
print("\nCounting down from 100 to 1:")
number = 100
while number >= 1:
    print(number)
    number -= 1
