print("Welcome to CIBT bank")
pin = int(input("Enter Pin: "))

if(pin == 12345):
    userBal = 10000
    while True:
        print("1 - Know your balance")
        print("2 - Withdraw money")
        print("3 - Deposit money")
        print("4 - Fast withdraw")
  
        userInp = int(input("Enter your choice: "))
        if(userInp > 5):
            print("Please enter valid input")
        else:
            if(userInp == 1):
                print("Your balance: ", userBal,"$")
                print("===================================")
            elif(userInp == 2):
                withdraw = int(input("Enter amount: "))
                if(withdraw <= userBal):
                    print(withdraw,"$", "Sucess")
                    newBal = userBal - withdraw
                    print("New Balance: ", newBal)
                    userBal = newBal
                    print("===================================")
                else:
                    print("Not enough Balance")
                    break
            elif(userInp == 3):
                deposit = int(input("Enter amount: "))
                newDepo = deposit + userBal
                print("Balance: ",newDepo)
                userBal = newDepo
                print("===================================")
            else:
                print("Fast withdraw")
                print("1- 500$")
                print("2- 1000$")
                print("3- 2000$")
                options = {"1":500, "2":1000, "3":2000}
                userFastOption = (input("Enter choice: "))
                for key in options.keys():
                    if(userFastOption == key):
                        print("Fast Cash", options[key])
                        newBalance = userBal - int(options[key])
                        print("Your balance",newBalance)
                        userBal = newBalance
                        print("===================================")
                
