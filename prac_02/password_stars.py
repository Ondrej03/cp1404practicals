MIN_PASS_LEN = 4

def main():
    password = get_password()

    print_password(password)


def print_password(password):
    print("*" * len(password))


def get_password():
    password = input("Type password: ")
    while len(password) < MIN_PASS_LEN:
        print(f"Password must contain at least {MIN_PASS_LEN} characters")
        password = input("Type password: ")
    return password


main()