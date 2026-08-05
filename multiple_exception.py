try:
    num1, num2 = eval(input("enter two number, separted by comma:  "))
    result = num1 / num2
    print("result is", result)


except ZeroDivisionError:
    print("division by zero is error!!!" )

except SyntaxError:
    print("comma is missing. enter numbeer separted by comma like this 1, 2")

except:
    print("wrong input")

else:
    print("No exception")

finally:
    print("this will execute no matter what")
    