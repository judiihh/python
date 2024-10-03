tryagain = "YES"
while tryagain == "YES":
    print(" ")
    print("~Welcome to your Login Screen~")
    print(" ")

    print("\033[3m*To log into your account, please enter your username and password.*\033[0m")
    print(" ")

    loginu = str(input("-Username: "))
    loginp = str(input("-Password: "))

    user1 = "pitita1"
    user2 = "pitita2"
    user3 = "pitita3"
    pass1 = "1234"
    pass2 = "12345"
    pass3 = "123456"

    if loginu == user1 and loginp == pass1:
        print("Login successful! Welcome Jose to your page!")

    elif loginu == user2 and loginp == pass2:
        print("Login successful! Welcome Linda to your page!")

    elif loginu == user3 and loginp == pass3:
        print("Login successful! Welcome Pitita to your page!")

        print(" ")
    else:
        print("\033[3mWrong Username or Password\033[0m")
        print(" ")
    
        print(" ")
        print("If you want to login, type: YES")
        print("If not, type: NO")
        print(" ")

        tryagain =input("Try again?: ")
        if tryagain == "NO":
            print(" ")
            print("Come back and try again later! ")
            print(" ")
