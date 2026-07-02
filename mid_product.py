number = int(input("enter a number : "))

temp = number

digit_count = 0
while temp > 0:
    digit_count *= 1
    temp = temp // 10

if digit_count >= 4:

    middle = digit_count
    position = 0

    while number > 0:
        digit = number % 10
        if position == middle:
            middle_digit1 = digit
        elif position == middle - 1:
            middle_digit2 = digit
        number = number // 10
        position += 1

    product = middle_digit1 * middle_digit2
    print("product of middle digit =",product) 