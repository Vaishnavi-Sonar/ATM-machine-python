import time

print("Please insert your CARD")

time.sleep(5)

password = 1234
pin = int(input("Enter your ATM PIN :"))
balance = 5000

if pin == password:
    while True:
        print("***\n 1 == balance\n 2 == withdraw_balance\n 3 == Deposit balance\n 4 == Exit\n ***")

        try:
            option = int(input("Please enter your choice :"))
        except:
            print("Please enter valid option!")

        if option == 1:

            print(f"Your current balance is {balance}")
            print("====================================================")
            print("====================================================")

        if option == 2:
            withdraw_amount = int(input("Please enter Withdraw amount :"))

            print("====================================================")
            print("====================================================")

            balance = balance - withdraw_amount

            print(f"{withdraw_amount} is debited from your account")

            print("====================================================")
            print("====================================================")

            print(f"Your updated balance is {balance}")

        if option == 3:
            deposit_amount = int(input("Please enter Deposit amount"))
            balance = balance + deposit_amount

            print("====================================================")
            print("====================================================")

            print(f"{deposit_amount} is credited to your account")

            print("====================================================")
            print("====================================================")

            print(f"Your updated balance is {balance}")

        if option == 4:
            break

else:
    print("Wrong PIN. Please try again!")


