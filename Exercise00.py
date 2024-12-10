peopleCount = int(input("How many people need a ride ? "))
taxiCount = int(input("How many people fit in one taxi? "))
print("Number of taxis needed:", (peopleCount // taxiCount) if (peopleCount % taxiCount == 0) else ((peopleCount // taxiCount) + 1) )