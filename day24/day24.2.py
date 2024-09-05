def main():
    print('--- For Loop Examples ---')

    # 1. Counting from 1 to 10
    print('Counting from 1 to 10:')
    for i in range(1, 11):
        print(i)
    
    # 2. Printing elements of a list
    print('Printing elements of a list:')
    fruits = ['Apple', 'Banana', 'Cherry']
    for fruit in fruits:
        print(fruit)
    
    # 3. Multiples of 10
    print('Multiples of 10 from 10 to 100:')
    for i in range(1, 11):
        print(i * 10)
    
    # 4. Printing even numbers from 1 to 20
    print('Even numbers from 1 to 20:')
    for i in range(2, 21, 2):
        print(i)
    
    # 5. Sum of numbers from 1 to 10
    print('Sum of numbers from 1 to 10:')
    total_sum = 0
    for i in range(1, 11):
        total_sum += i
    print(total_sum)
    
    # 6. Squares of numbers from 1 to 5
    print('Squares of numbers from 1 to 5:')
    for i in range(1, 6):
        print(f'Square of {i} is {i * i}')
    
    # 7. Printing a list in reverse order
    print('List in reverse order:')
    for fruit in reversed(fruits):
        print(fruit)
    
    # 8. Fibonacci sequence up to 10 terms
    print('Fibonacci sequence up to 10 terms:')
    a, b = 0, 1
    for _ in range(10):
        print(a)
        a, b = b, a + b
    
    # 9. Factorial of numbers from 1 to 5
    print('Factorial of numbers from 1 to 5:')
    for i in range(1, 6):
        factorial = 1
        for j in range(1, i + 1):
            factorial *= j
        print(f'Factorial of {i} is {factorial}')
    
    # 10. Finding prime numbers up to 20
    print('Prime numbers up to 20:')
    for num in range(2, 21):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)

    print('--- While Loop Examples ---')

    # 1. Counting from 1 to 10
    print('Counting from 1 to 10:')
    i = 1
    while i <= 10:
        print(i)
        i += 1
    
    # 2. Printing elements of a list
    print('Printing elements of a list:')
    fruits = ['Apple', 'Banana', 'Cherry']
    i = 0
    while i < len(fruits):
        print(fruits[i])
        i += 1
    
    # 3. Multiples of 10
    print('Multiples of 10 from 10 to 100:')
    i = 1
    while i <= 10:
        print(i * 10)
        i += 1
    
    # 4. Printing even numbers from 1 to 20
    print('Even numbers from 1 to 20:')
    i = 2
    while i <= 20:
        print(i)
        i += 2
    
    # 5. Sum of numbers from 1 to 10
    print('Sum of numbers from 1 to 10:')
    total_sum = 0
    i = 1
    while i <= 10:
        total_sum += i
        i += 1
    print(total_sum)
    
    # 6. Squares of numbers from 1 to 5
    print('Squares of numbers from 1 to 5:')
    i = 1
    while i <= 5:
        print(f'Square of {i} is {i * i}')
        i += 1
    
    # 7. Printing a list in reverse order
    print('List in reverse order:')
    i = len(fruits) - 1
    while i >= 0:
        print(fruits[i])
        i -= 1
    
    # 8. Fibonacci sequence up to 10 terms
    print('Fibonacci sequence up to 10 terms:')
    a, b = 0, 1
    count = 0
    while count < 10:
        print(a)
        a, b = b, a + b
        count += 1
    
    # 9. Factorial of numbers from 1 to 5
    print('Factorial of numbers from 1 to 5:')
    i = 1
    while i <= 5:
        factorial = 1
        j = 1
        while j <= i:
            factorial *= j
            j += 1
        print(f'Factorial of {i} is {factorial}')
        i += 1
    
    # 10. Finding prime numbers up to 20
    print('Prime numbers up to 20:')
    num = 2
    while num <= 20:
        is_prime = True
        i = 2
        while i < num:
            if num % i == 0:
                is_prime = False
                break
            i += 1
        if is_prime:
            print(num)
        num += 1

# Call the main function to execute the code
if __name__ == '__main__':
    main()