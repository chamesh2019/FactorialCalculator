def calculateFactorial(limit):
    factorial = 1
    for i in range(1, limit + 1):
        factorial *= i
    return factorial

if __name__ == "__main__":
    limit = input("Enter a number: ")
    print(calculateFactorial(limit))