import time  # Import the time module to use sleep function

# Take the number as input
number = int(input("Enter the number of seconds: "))

# Use a while loop for the countdown
while number >= 0:
    print(number)
    time.sleep(1)  # Wait for 1 second
    number -= 1
