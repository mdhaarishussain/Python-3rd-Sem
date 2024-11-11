try:
    age = int(input("Enter the age: "))
    if age < 0:
        raise ValueError("Age cannot be negative")
    else:
        print(f"The age is: {age}")
except ValueError as ve:
    print(f"Error: {ve}")