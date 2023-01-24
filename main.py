usernameInput = input("USERNAME : ")
passwordInput = input("PASSWORD : ")
S1 = 10000
S2 = 20000
S3 = 30000
if usernameInput == "admin" and passwordInput == "1129":
    print("----- WELCOME TO NGILITY SHOP -----")
    print("1. Data S1 x1 = 10,000 THB")
    print("2. Data S2 x1 = 20,000 THB")
    print("3. Data S3 x1 = 30,000 THB")
    print("-----------------------------------")
    userSelected = int(input(">>"))
    if userSelected == 1:
        price = int(input("Price (THB): "))
        vat = 7
        result = price + (price * 7 / 100)
        print(result)

    elif userSelected == 2:
        price1 = int(input("First Product Price : "))
        price2 = int(input("Second Product Price : "))
        print("price1+price2")