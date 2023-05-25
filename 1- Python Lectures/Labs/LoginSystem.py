
TrailCounter = 0
while(TrailCounter != 3):
    
    UserName = input("Please Enter Your Username: ")
    Password = input("Please Enter Your Password: ")

    if UserName == "Ahmed":
        if int(Password) == 123:
            print("Welcome " +  UserName)
            break

    elif UserName == "Ali":
        if int(Password) == 456:
            print("Welcome " + UserName)
            break

    elif UserName == "Amr":
        if int(Password) == 789:
            print("Welcome " + UserName)
            break
    else:
        TrailCounter += 1
        print("Incorrect Username or Password, Please Try Again")
        print(str(3-TrailCounter) + " Trail(s) left!")
else:
    print("Sorry, The trails are ended, please contact to your administrator")