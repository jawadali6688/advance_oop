class Calculator:

    def __init__(self):

        print("Calculator started...")


        while True:

            print("Select an option")
            print("1. Add two numbers")
            print("2. Subtract two numbers")
            print("3. Multiply two numbers")

            choice = int(input("Enter Your Choice: "))

            if choice == (3 or "3"):
                print("Program is terminated")
                break 


cal = Calculator()
