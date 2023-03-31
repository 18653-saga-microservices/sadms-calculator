class Calculator:
    def Add(a, b):
        result = a + b
        return result

    def Multiply(a, b):
        result = a * b
        return result

    def Subtract(a, b):
        result = a - b
        return result

    def Divide(a, b):
        result = a / b
        return result


if __name__ == "__main__":
    c = Calculator.Add(1, 2)
    print(c)