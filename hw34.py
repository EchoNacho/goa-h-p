def simple_calculator(num1, num2, operation):
    if operation == "pluse":
        return num1 + num2
    elif operation == "minuse":
        return num1 - num2
    elif operation == "times":
        return num1 * num2
    elif operation == "devide":
        if num2 == 0:
            return "mistake: deviding zero is inpssible"
        else:
            return num1 / num2
    else:
        return "mistake: wrong operation"

# ფუნქციის გამოძახება და შედეგების ბეჭდვა სხვადასხვა ოპერაციებით
print(simple_calculator(10, 5, "pluse"))     # უნდა დაბეჭდოს: 15
print(simple_calculator(10, 5, "minuse"))    # უნდა დაბეჭდოს: 5
print(simple_calculator(10, 5, "times"))   # უნდა დაბეჭდოს: 50
print(simple_calculator(10, 0, "devide"))       # უნდა დაბეჭდოს: შეცდომა: ნულზე გაყოფა შეუძლებელია
print(simple_calculator(10, 5, "devide"))       # უნდა დაბეჭდოს: 2.0
print(simple_calculator(10, 5, "identification"))  # უნდა დაბეჭდოს: შეცდომა: არასწორი ოპერაცია
