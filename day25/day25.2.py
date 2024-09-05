def for_loop_examples():
    print('--- For Loop Examples ---')

    # 1. Counting from 1 to 10
    print('Counting from 1 to 10:')
    for i in range(1, 11):
        print(i)
    
    # 2. Printing array elements
    print('Array elements:')
    fruits = ['Apple', 'Banana', 'Cherry']
    for fruit in fruits:
        print(fruit)
    
    # 3. Printing multiples of 10
    print('Multiples of 10 from 10 to 100:')
    for i in range(1, 11):
        print(i * 10)
    
    # 4. Printing names containing 'A'
    print('Names containing "A":')
    names = ['Alice', 'Bob', 'Charlie']
    for name in names:
        if 'A' in name:
            print(name)
    
    # 5. Printing days of the month (assuming 30 days)
    print('Days of the month:')
    for day in range(1, 31):
        print(f'Day {day}')
    
    # 6. Sum of numbers between two values
    print('Sum of numbers between 5 and 7:')
    num1, num2 = 5, 7
    total_sum = sum(range(num1, num2 + 1))
    print(f'Sum from {num1} to {num2} is {total_sum}')
    
    # 7. Printing squares of numbers from 1 to 10
    print('Squares of numbers from 1 to 10:')
    for i in range(1, 11):
        print(f'Square of {i} is {i * i}')
    
    # 8. Reverse printing of an array
    print('Reversed array elements:')
    for fruit in reversed(fruits):
        print(fruit)
    
    # 9. Fibonacci series up to 10 numbers
    print('Fibonacci series up to 10 numbers:')
    a, b = 0, 1
    for _ in range(10):
        print(a)
        a, b = b, a + b
    
    # 10. Factorial of 5
    print('Factorial of 5:')
    factorial = 1
    for i in range(1, 6):
        factorial *= i
    print(f'Factorial of 5 is {factorial}')

# Call the function to see for loop examples
for_loop_examples()
