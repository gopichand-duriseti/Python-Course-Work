data={'1234':{'balance':45678,'pin':123,'history':[]},
      '5678':{'balance':56789,'pin':123,'history':[]},
      '5612':{'balance':98798,'pin':123,'history':[]},
      '2345':{'balance':45678,'pin':123,'history':[]},
      '6789':{'balance':19876,'pin':123,'history':[]},
}
def Welcome():
    print("Welcome to the ATM".center(40,'-'))
def menu():
    print('1.Check Balance')
    print('2.Deposit')
    print('3.Withdraw')
    print('4.View Transaction')
    print('0.Exit')
acc_num=None
Login_status=False
def login(acc_no,pin):
    if acc_no in data:
        if data[acc_no]['pin']==pin:
            global acc_num
            global Login_status
            acc_num=acc_no
            Login_status=True
            print("Login Succesful")
            return True
        else:
            print("Invalid PIN")
            return False
    else:
        print("Invalid Account Number")
        return False
   
def check_balance():
    if Login_status and acc_num:
        print(f'Current Balance:{data[acc_num]['balance']}')
    else:
        print("Login Again")
def deposit():
    if Login_status and acc_num:
        amt=int(input("Enter the amount to deposit: "))
        data[acc_num]['balance']+=amt
        data[acc_num]['history'].append(f'Deposited:${amt}')
        print(f'{amt} is successfully deposit')
    else:
        print("Login Again")
def withdraw():
    if Login_status and acc_num:
        amt=int(input("Enter the amount to Withdraw: "))
        if amt<=data[acc_num]['balance']:
            data[acc_num]['balance']-=amt
            data[acc_num]['history'].append(f'WithDraw:${amt}')
            print(f'{amt} is successfully Withdraw')
        else:
            print("Insufficient Balance")
    else:
        print("Login Again")
def view_transactions():
    if Login_status and acc_num:
        if data[acc_num]['history']:
            print("\nTransactions: ")
            for i in data[acc_num]['history']:
                print(i)
            print("End of transactions")
        else:
            print("No Transactions")