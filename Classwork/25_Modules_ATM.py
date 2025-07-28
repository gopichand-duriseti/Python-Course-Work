data={'1234':{'balance':45678,'pin':123,'history':[]},
      '5678':{'balance':56789,'pin':123,'history':[]},
      '5612':{'balance':98798,'pin':123,'history':[]},
      '2345':{'balance':45678,'pin':123,'history':[]},
      '6789':{'balance':19876,'pin':123,'history':[]},
}
acc_num=None
def login(acc_no,pin):
    if acc_no in data:
        if data[acc_no]['pin']==pin:
            acc_num=acc_no
            print("Login Succesful")
        else:
            print("Invalid PIN")
    else:
        print("Invalid Account Number")
   


