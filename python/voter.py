age=int(input("Enter age..."))
Citizen=False
if Citizen:
    if age>=18:
        print("Eligible to vote")
    else:
        print("Minimum age is met")
else:
    print("Not Eligible for vote")