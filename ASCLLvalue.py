ch = input("Enter one character: ")

if len(ch) != 1:
    print("Please enter exactly one character.")
else:
    print("ASCII value:", ord(ch))

    if ch >= 'A' and ch <= 'Z':
        print("Character type: Uppercase letter")

    elif ch >= 'a' and ch <= 'z':
        print("Character type: Lowercase letter")

    elif ch >= '0' and ch <= '9':
        print("Character type: Digit")

    else:
        print("Character type: Special character")