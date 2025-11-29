#Calculator with basic operations
def add(a: float, b: float) -> float:
    #Add two numbers.
    return a + b

def subtract(a: float, b: float) -> float:
    #Subtract b from a.
    return a - b

def multiply(a: float, b: float) -> float:
    #Multiply two numbers.
    return a * b

def divide(a: float, b: float) -> float:
    #Divide a by b. Raises ValueError on division by zero.
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def main():
    while True:
        print("what would you like to do ? \n 0: exit \n 1: Add \n 2: Subtract \n 3: Multiply \n 4: Divide")
        choice = input().strip()

        if choice == '0':
            print("Goodbye")
            break

        print("Enter your first number : ")
        num1 = int(input())
        print("Enter your second number : ")
        num2 = int(input())

        if choice == '1':
            print(f"Result: {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {divide(num1, num2)}")
        else:
            print("Invalid Option")

        print("---------------------------------")

if __name__ == "__main__":
    main()

print("hello word - for demo purposes ")