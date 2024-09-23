num_of_items = int(input("Number of items: "))
if num_of_items <= 0:
    print("Invalid number of items!")
else:
    total_sum = 0
    for i in range(0, num_of_items):
        item_price = float(input("Price of item: "))
        total_sum += item_price

    if total_sum > 100:
        total_sum *= 0.9

    print(f"Total price for {num_of_items} items is ${total_sum:.2f}")