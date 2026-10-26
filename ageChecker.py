age =int(input("Enter your age: "))
hasIdCard=input("Do you have an ID card? (yes/no): ")
if age >= 18 and hasIdCard.lower() == "yes":
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

if age >= 13 and age <= 19:
    print("You are a teenager.")
else:
    print("You are an adult.")