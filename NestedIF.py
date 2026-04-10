age = int(input("Enter your name:"))
if age >=18:
    registered_voter = input("Are you a registered voter?(True/False):")
    registered_voter = registered_voter.lower()
    if registered_voter == "true":
        print("You are eligible to vote.")
    else:
        print("you need to register to vote.")
else:
    print("you are not eligible to vote.")
    
