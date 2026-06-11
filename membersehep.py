print("enter marks obtained in 5 subjects: ")
markOne = int(input())
marktwo = int(input())
markthree = int(input())
markfour = int(input())
markfive = int(input())
tot = markOne + marktwo + markthree + markfour + markfive
avg = int(tot / 5 )
validrange = range(0,101)
if avg not in validrange:
    print("invalid input")
elif avg in range(91,101):
    print("your greade is A1")
elif avg in range(81,91):
    print("your greade is A2")
elif avg in range(61,81):
    print("your greade is B1")
elif avg in range(51,61):
    print("your greade is C1")
elif avg in range(33,51):
    print("your greade is C")
elif avg in range(00,33):
    print("your greade is E1")