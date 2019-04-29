import getpass

num = 3
PIN = "1234"
for i in range(1, num+1):
    supplied_pin = getpass.getpass("Enter your PIN:")
    if supplied_pin == PIN:
        print("password correct!")
        break
    else:
        print("wrong password","it was your", i, "attemp, you have", num - i, "chances")
        if num - i == 0:
            print("you are not allow to enter any more in your life")

