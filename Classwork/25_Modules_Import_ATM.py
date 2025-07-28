import ModuleATM_25 #if (from ModuleATM_25 import *) then no need of mentioning the file name again and again
#import ModuleATM_25 as atm :-Alias name
ModuleATM_25.Welcome()
acc_no=input("Enter the account number: ")
pin=int(input("Enter the pin: "))
while True:
    if ModuleATM_25.login(acc_no,pin):
        ModuleATM_25.menu()
        op=int(input("Select the option: "))
        if op==0:
            print("Thank you")
            break 
        elif op==1:
            ModuleATM_25.check_balance()
        elif op==2:
            ModuleATM_25.deposit()
        elif op==3:
            ModuleATM_25.withdraw()
        elif op==4:
            ModuleATM_25.view_transactions()
    else:
        break