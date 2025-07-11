g=['pic1','pic2','pic3','pic4']
for i in range(len(g)):
    print(f'{i+1}. {g[i]}')
s=set(map(int,input("enter the photo number: ").split(',')))

for i in s:
    print(g[i])
print()

#GRADING
data={1:{'name':'Dinesh','exam_status':True,'python':100,'sql':95,'html':98},
      2:{'name':'Charan','exam_status':True,'python':80,'sql':45,'html':68},
      3:{'name':'Arun','exam_status':False,'python':None,'sql':None,'html':None},
      4:{'name':'Gopal','exam_status':True,'python':30,'sql':15,'html':25},
      5:{'name':'Gopi','exam_status':True,'python':80,'sql':75,'html':65}}


for i in data.keys():
    print(f'{i}. {data[i]["name"]}')
    
studid=int(input("Enter the student Id: "))
if studid in data:
    if data[studid]["exam_status"]:
        #print(data[studid])
        avg=(data[studid]['python']+data[studid]['sql']+data[studid]['html'])/3
        if avg>90:
            print(f'Congrats!!!\n{data[studid]["name"]} got "A" grade')
        elif avg>75:
            print(f'Good!!!\n{data[studid]["name"]} got "B" grade')
        elif avg>50:
            print(f'Need Improvement!!!\n{data[studid]["name"]} got "C" grade')
        else:
            print(f'{data[studid]["name"]}-Failed,Better luck next time')
    else:
        print(f'{data[studid]["name"]} is not attempted the exams')
else:
    print("The id is not present.Try Again!")
print()

#ROCK-PAPER-SCISSOR
import random
print('1.Rock\n2.Paper\n3.Scissor')

while True:
    ch=int(input("Enter your choice: "))
    if ch==0:
        print("Game Over")
        break
    elif ch==1:
        com=random.randint(1,3)
        print("computer choice:",com)
        if com==1:
            print("Tie both choose the Rock")
        elif com==2:
            print("Computer Wins")
        elif com==3:
            print("You Win")
    elif ch==2:
        com=random.randint(1,3)
        print("computer choice:",com)
        if com==1:
            print("You Win")
        elif com==2:
            print("Tie both choose the Paper")
        elif com==3:
            print("Computer Wins")
    elif ch==3:
        com=random.randint(1,3)
        print("computer choice:",com)
        if com==1:
            print("Computer Wins")
        elif com==2:
            print("You Win")
        elif com==3:
            print("Tie both choose the Scissor")
    
    else:
        print("Invalid Choice")
