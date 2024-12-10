totalAmount = float(input("Total Amount: "))
itemsCount = int(input("Number of Items: "))
day = input("Day of the week: ")
discount: float

if (day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]):
    discount = 0.1
elif (day in ["Saturday", "Sunday"]):
    discount = 0.2
else:
    print("Invalid day!\nExiting...")
    exit(1)

discount += 0.05 * (itemsCount > 5)

print(f"Total price after discount is: {totalAmount * (1 - discount)} dinars.")