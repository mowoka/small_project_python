


print("Welcome to Calculator Python")
print("please input first number")
num1 = int(input())
print("please input operator")
operate = input()
print("please input second number")
num2 = int(input())

if operate == "+":
    result = num1 + num2
if operate == "-":
    result = num1 - num2
if operate == "/":
    result = num1 / num2
if operate == "*":
    result = num1 * num2
if operate == "**":
    result = num1 ** num2

print(f'Result for {num1} {operate} {num2} = {result}')