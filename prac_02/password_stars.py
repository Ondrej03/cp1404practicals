MIN_PASS_LEN = 4

password = input("Type password: ")
while len(password) < MIN_PASS_LEN:
    print(f"Password must contain at least {MIN_PASS_LEN} characters")
    password = input("Type password: ")

print("*" * len(password))

