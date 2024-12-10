print("Runner 1:")
name0 = input("Name: ")
Time0 = float(input("Time (in seconds): "))

print("Runner 2:")
name1 = input("Name: ")
Time1 = float(input("Time (in seconds): "))

if (Time0 < Time1):
    print("The faster runner is", name1)
elif (Time0 > Time1):
    print("The faster runner is", name0)
else:
    print(f"{name0} And {name1} have the sime time")