
from utils.addition import addition
from utils.subtraction import subtraction
from utils.multiplication import multiplication
from utils.division import division

def main():
    
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))

    
    print(f"Addition: {addition(a, b)}")
    print(f"Subtraction: {subtraction(a, b)}")
    print(f"Multiplication: {multiplication(a, b)}")
    print(f"Division: {division(a, b)}")


if __name__ == "__main__":
    main()
