var = input("Please enter an integer: ")
if not var.isdecimal():
    print("ERROR, input not decimal")
    exit(1)
else:
    for i in range(int(var), -11, -2):
        print(i)
