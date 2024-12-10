firstAge = int(input("Please type in the age of the first person: "))
secondAge = int(input("Please type in the age of the second person: "))
if (firstAge < 0 or secondAge < 0):
    print("Invalid age!")
    exit(1)
    
resultString = (firstAge != secondAge) * f"The older age is: {max(firstAge, secondAge)}" + (firstAge == secondAge) * "Both people are the same age!"

print(resultString)