def main():
    # Variables
    a = 5
    b = 10
    name = "Alice"
    age = 25
    height = 5.9
    is_student = True
    x, y = 2, 3
    total = a + b
    greeting = "Hello, " + name
    balance = 1000.50
    
    # Variable Data Types
    num = 42               # Integer
    pi = 3.14159           # Float
    message = "Hello!"     # String
    flag = True            # Boolean
    colors = ["red", "green", "blue"]  # List
    coordinates = (10, 20)  # Tuple
    person = {"name": "John", "age": 30}  # Dictionary
    unique_numbers = {1, 2, 3}  # Set
    complex_num = 2 + 3j  # Complex number
    nothing = None        # NoneType
    
    # Input
    user_name = input("Enter your name: ")
    user_age = int(input("Enter your age: "))
    user_height = float(input("Enter your height in meters: "))
    is_student = input("Are you a student? (yes/no): ") == "yes"
    user_number = int(input("Enter a number: "))
    user_city = input("Enter your city: ")
    user_email = input("Enter your email address: ")
    user_phone = input("Enter your phone number: ")
    user_score = float(input("Enter your score: "))
    user_color = input("Enter your favorite color: ")

    # Comparison Operators
    print(5 == 5)      # True
    print(5 != 3)      # True
    print(10 > 7)      # True
    print(5 < 8)       # True
    print(10 >= 10)    # True
    print(4 <= 5)      # True
    print("apple" == "apple")  # True
    print("apple" != "orange")  # True
    print(5 == 5.0)    # True
    print([1, 2, 3] == [1, 2, 3])  # True

    # Logical Operators
    print(True and False)  # False
    print(True or False)   # True
    print(not True)        # False
    print((5 > 3) and (2 < 4))  # True
    print(not (5 > 3 and 2 < 4))  # False
    print(not (5 < 3 or 2 < 4))  # False
    print((10 > 5) or (7 < 3) and (5 != 4))  # True
    print(not (4 == 4))  # False
    print((3 > 2) and (not (5 == 5)))  # False
    print((10 > 5) and (2 < 4) or (7 > 3))  # True

    # Loops
    for i in range(5):
        print(i)
    
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print(fruit)
    
    i = 0
    while i < 3:
        print(i)
        i += 1

    for index, value in enumerate(fruits):
        print(index, value)
    
    i = 0
    while True:
        if i >= 3:
            break
        print(i)
        i += 1
    
    for i in range(2):
        for j in range(3):
            print(i, j)
    
    i = 0
    while i < 5:
        if i == 3:
            i += 1
            continue
        print(i)
        i += 1
    
    squares = [x**2 for x in range(5)]
    print(squares)
    
    i = 0
    count = 0
    while count < 5:
        count += 1
        i += count
    print(i)
    
    for char in "hello":
        print(char)

    # Conditional Statements
    x = 10
    if x > 5:
        print("x is greater than 5")

    x = 4
    if x > 5:
        print("x is greater than 5")
    else:
        print("x is not greater than 5")

    x = 10
    if x > 15:
        print("x is greater than 15")
    elif x > 5:
        print("x is greater than 5 but not greater than 15")
    else:
        print("x is 5 or less")

    x = 10
    if x > 5:
        if x < 15:
            print("x is between 5 and 15")

    x = 10
    message = "x is greater than 5" if x > 5 else "x is 5 or less"
    print(message)

    x = 7
    if x > 5 and x < 10:
        print("x is between 5 and 10")

    x = 4
    if x < 5 or x == 10:
        print("x is either less than 5 or equal to 10")

    color = "blue"
    if color in ["red", "green", "blue"]:
        print("Color is one of the primary colors")

    color = "yellow"
    if color not in ["red", "green", "blue"]:
        print("Color is not a primary color")

    is_active = True
    if is_active:
        print("The system is active")

    # Lists
    numbers = [1, 2, 3, 4, 5]
    print(numbers[0])  # Output: 1
    numbers[1] = 10
    numbers.append(6)
    numbers.remove(3)
    print(numbers[1:4])  # Output: [10, 4, 6]
    
    for number in numbers:
        print(number)
    
    squares = [x**2 for x in numbers]
    print(squares)
    
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(len(numbers))  # Output: 5

    # Indexing
    print(numbers[0])  # Output: 1
    print(numbers[-1])  # Output: 5 (last element)
    print(numbers[1:4])  # Output: [10, 4, 6]
    print(fruits[1])  # Output: banana
    print(fruits[-2])  # Output: banana (second last element)
    print(fruits[:2])  # Output: ['apple', 'banana']
    print(fruits[1:])  # Output: ['banana', 'cherry']
    print(fruits[::-1])  # Output: ['cherry', 'banana', 'apple']
    print(fruits[::2])  # Output: ['apple', 'cherry']
    print(matrix[1][2])  # Output: 6
    print(colors[0])  # Output: red

if __name__ == "__main__":
    main()