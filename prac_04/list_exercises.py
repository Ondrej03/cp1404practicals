def main():
    numbers = []
    while len(numbers) != 5:
        try:
            numbers.append(int(input("Number: ")))
        except ValueError:
            print("Invalid number")


    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {(sum(numbers) / len(numbers)):.2f}")

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']

    if input("Input you username: ") in usernames:
        print("Access granted")
    else:
        print("Access denied")


main()