FirstNumber = int(input("What is the first number? >  "))
SecondNumber = input("What is the second number? > ")

print(FirstNumber, "+", SecondNumber, "= {}".format(int(FirstNumber) + int(SecondNumber)))
print(FirstNumber, "*", SecondNumber, "= {}".format(int(FirstNumber) * int(SecondNumber)))
print(FirstNumber, "-", SecondNumber, "= {}".format(int(FirstNumber) - int(SecondNumber)))
print(FirstNumber, "/", SecondNumber, f"= {int(FirstNumber) / int(SecondNumber):.{1}f}")
