print("            ONLINE BANKING MANAGEMENT SYSTEM  ")
print("            ********************************  ")
input(" NAME  : ")
input(" SURNAME  :  ")
input(" ACCOUNT  :  ")
input(" EMAIL : ")


def details():
    print("PLEASE FILL INN ALL YOUR INFORMATION TO BE REGISTERED SUCCESSFUL")

def deposit():
    balance=5000
    deposit = input("How much do you wamt to deposit: $")
    deposit = float(deposit)

    new_balance = balance + deposit
    print ("You've successfully deposited $ {} into BMS . Your new balance is {}.".format(deposit, new_balance))
    return new_balance

#withdrawal part
def withdraw():
    balance=5000
    money=3
    amount=input ("Please enter amount to withdraw:: ")
    amount=int(amount)
    if amount> balance:
        print ("Your transpressions exceeds the current balance!. TRY AGAIN!!")
    elif amount== balance:
        print("Mind you try to reduce your amnt.You need to have ${} in your account". format(money))
    elif (amount < balance) and (amount!=balance) :
        balanced=balance-amount
        return balanced
    else:
        print("OOOPs BUMMER")

#This is an obvious one, this is where you check your balance.
def bank_balance():

    print( "Balance: $", balance)
    return balance

def main():
    print("""
    [1] - Banking Details 
    [2] - Deposit
    [3] - Withdrew
    [4] - Balance Request
    [5] - Exit
    """)
    balance= input ('PLEASE confirm YOUR ACCOUNT BALANCE): ')
    press = input('What would you Like to Do? PLEASE SELECT ONE OF THE CHOICES ABOVE!!: ')

    if press == '1':
        datails()
    elif press == '2':
        deposit()
    elif press == '3':
        withdraw()
    elif press == '4':
        bank_balance()
    elif press == '5':  # this line exits the program (by selecting option )
        log= input("YOU ARE ABOUT TO EXIT? Y/N? ").upper()
        if log == 'Y':
            exit()
        else:
            main()
    else:
        print('No Valid Choice Was Chosen!')
main( )
