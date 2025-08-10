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
# my_module.py
'''def greet(name):
return f"Hello, {name}!"
if __name__ == "__main__":
print(greet("Alice")) # Executes only when this file is
run directly
#output will be Hello, name without calling function or giving name if you run in this file(Hello, Alice)
#ELSE you have to give name in other file after importing(if not giving name some error will come)


● If you run: python my_module.py → the block executes
● If you import it in another file → the block is ignored'''