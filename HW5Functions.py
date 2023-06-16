def involve(number, degree):
    if degree == 1:
        return number
    else:
        return number * involve(number, degree - 1)


def sum(num1, num2):
    if num2 == 0:
        return num1
    else:
        return sum(num1, num2 - 1) + 1
