username = input("User : ")
password = input("Password : ")
if username == "admin" and password == "4321" :
    print("Welcome to system")
    print("Please Select your fuction")
    print("1. Tax Calculation")
    print("2. OT Calculation")
    choice = input("Select : ")
    if choice == "1" :
      item_price = int(input("item price : "))
      vat = 7
      result = item_price+(item_price*vat/100)
      print("Item price : ",result)

    elif choice == "2":
        salary = int(input("your salary : "))
        ot = int(input("Hours : "))
        DOM = 22
        working_time = 8
        result2 = ((salary/(DOM*working_time))*3)*ot
        print(int(result2),"Bath")
    else:
        print("Error")
else:
    print("You are not Admin")