
#1
name = input("Input your name :")
out_file = open("name.txt", "w")
out_file.write(name)
out_file.close()

#2
out_file = open("name.txt", "r")
name = out_file.read()
print(f"Hi {name}!")
out_file.close()

#3
NUMBERS = [17, 42, 400]

out_file = open("numbers.txt", "w")
for number in NUMBERS:
    out_file.write(str(number) + "\n")
out_file.close()

with open("numbers.txt") as out_file:
    num_sum = 0
    for _ in range(2):
        num_sum += int(out_file.readline())

print(num_sum)

with open("numbers.txt") as out_file:
    row_sum = 0
    for _ in out_file:
        row_sum += 1

print(row_sum)