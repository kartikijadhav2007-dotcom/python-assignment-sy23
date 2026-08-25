# Simple Calculator

print("===== SIMPLE CALCULATOR =====")

# Get numbers from the user
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nChoose a calculation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Advanced Calculations")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print("Result =", num1 + num2)

    elif choice == "2":
        print("Result =", num1 - num2)

    elif choice == "3":
        print("Result =", num1 * num2)

    elif choice == "4":
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            print("Result =", num1 / num2)

    elif choice == "5":
        print("\nAdvanced Calculations")
        print("1. Exponentiation")
        print("2. Modulus")

        advanced_choice = input("Enter your choice (1-2): ")

        if advanced_choice == "1":
            print("Result =", num1 ** num2)

        elif advanced_choice == "2":
            if num2 == 0:
                print("Error: Cannot use zero as the divisor.")
            else:
                print("Result =", num1 % num2)

        else:
            print("Invalid choice.")

    else:
        print("Invalid choice. Please enter a number from 1 to 5.")

except ValueError:
    print("Invalid input! Please enter numbers only.")

print("\n===== PROGRAM ENDED =====")