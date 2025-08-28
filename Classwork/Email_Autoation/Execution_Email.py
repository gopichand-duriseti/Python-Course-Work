import Email_Automation

subject = input("Enter email SUbject: ")
body = input("Enter email body: ")

choice=input("Do you want to send (1) Single Email or (2) Bulk Emails?Enter your choice(1 or 2): ")
if choice=='1':
    recipent=input("Enter recipent email: ")
    Email_Automation.send_email(recipent,subject,body)
elif choice == '2':
    csv_file=input("Enter the to CSV file with email addresses: ")
    Email_Automation.send_bulk_email(csv_file,subject,body)
else:
    print("Invalid Choice! Please enter 1 or 2.")
