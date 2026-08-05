
try:
    number = int(input("enetr a number:  "))
    print ("the number entered is ", number)

except ValueError as  ex:
    print("exceptoin ",ex)