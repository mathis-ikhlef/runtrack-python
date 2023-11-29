def calcule(num1, operator, num2):
    num1 = int(num1)
    num2 = int(num2)

    if operator == "+":
        return num1 + num2
    if operator == "-":
        return num1 - num2
    if operator == "*":
        return num1 * num2
    if operator == "/":
        return num1 / num2
    if operator == "%":
        return num1 % num2
    return "Invalid operator"


print(calcule(1, "+", 2))
print(calcule(1, "-", 2))
print(calcule(1, "*", 2))
print(calcule(1, "/", 2))
print(calcule(1, "%", 2))
print(calcule("4", "p", "4"))