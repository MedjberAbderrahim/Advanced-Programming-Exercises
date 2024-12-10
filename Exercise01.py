ticketPrice = 15.5
name = input("Please Enter your name: ")
if(name == "VIP"):
    print("Enjoy the show for free!")
else:
    ticketsCount = int(input("How many tickets would you like to buy? "))
    print(f"The total cost is {ticketsCount * ticketPrice}\nEnjoy your tickets!")