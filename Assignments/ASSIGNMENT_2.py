'''
'Did anyone finish the assignment?',
    "Not yet, I'm planning to do it tonight.",
    'I finished it yesterday. Took me forever!',
    'Wow, good job Charlie!',
    "You're always so fast, Charlie.",
    'I just wanted to get it out of the way.',
    'I might need help with question 4.',
    'I struggled with that one too.',
    'I can help both of you after lunch.',
    'Thanks, that would be awesome!'
'''

'''
nm=int(input("Enter the number of messages: "))
for i in range(nm):
    name,message=input().split(':')
    if name not in list(d.keys()):
        d[name]=[message] #or [(i,message)]
        d1.append(message)
    else:
        d[name].append(message) #or d[name].append((i,message))
        d1.append(message)
'''

d = {
    'Alice': [
        'Did anyone finish the assignment?',
        'Wow, good job Charlie!',
        'I might need help with question 4.',
        'Thanks, that would be awesome!'
    ],
    'Bob': [
        "Not yet, I'm planning to do it tonight.",
        "You're always so fast, Charlie.",
        'I struggled with that one too.'
    ],
    'Charlie': [
        'I finished it yesterday. Took me forever!',
        'I just wanted to get it out of the way.',
        'I can help both of you after lunch.'
    ]
}
d1= [
    'Did anyone finish the assignment?',
    "Not yet, I'm planning to do it tonight.",
    'I finished it yesterday. Took me forever!',
    'Wow, good job Charlie!',
    "You're always so fast, Charlie.",
    'I just wanted to get it out of the way.',
    'I might need help with question 4.',
    'I struggled with that one too.',
    'I can help both of you after lunch.',
    'Thanks, that would be awesome!']
k=list(d.keys())
def Total_messages():
    print(f'The total number of messages: {len(d1)}')
    print()
def Unique_Users():
    print(f'Unique users in the chatlist: {list(d.keys())}')
    print()
def Total_Words():
    sum1=0
    for i in d1:
        for j in i.split():
            sum1+=1
    print(f'Total words in the chat: {sum1}')
    print()
def Average_Words_Per_Message():
    sum2=0
    sum3=0
    for i in d1:
        for j in i.split():
            sum2+=1
    for i in d.values():
        sum3+=len(i)
    print(f'Average words per message: {sum2/sum3 :.2f}')
    print()
def Longest_Message():
    max=0
    for i in d1:
        if len(i)>max:
            max = len(i)
            s=i
    print(f'The longest message sent: {s}={len(i)}')
    print()
def Most_active_user():
    x=[]
    p=max([len(i) for i in d.values()])
    for i in d.keys():
        if len(d[i])==p:
            x.append(i)
    if len(x)>1:
        print(f'The most active user: {sorted(x)}')
    else:
        print(f'The most active user: {sorted(x)[0]}')
    print()
def Message_count_user():
    msg_c=input("Enter name: ")
    for i in d.keys():
        if i==msg_c:
            print(f'Message count for {msg_c}: {len(d[i])}')
    print()
def Most_frequent_word_user():
    from collections import Counter
    import string
    msg_f=input("Enter user name: ")
    punct_to_remove = string.punctuation.replace("'", "")
    for i,j in d.items():
        if i==msg_f:
            if len(j)>1:
                u=' '.join(d[i])
                u1=u.translate(str.maketrans('', '', punct_to_remove))
            else:
                u1=j[0].translate(str.maketrans('', '', punct_to_remove))
    r=Counter(u1.split())
    v=sorted(r, key=r.get,reverse=True)[0]
    print(f'The most frequently used word by {msg_f} is "{v}"')
    print()
def First_Last_msg_user():
    f_l_m=input("Enter user: ")
    for i,j in d.items():
        if i == f_l_m:
            print(f'The first message sent by {f_l_m}: {d[i][0]}')
            print(f'The last message sent by {f_l_m}: {d[i][-1]}')
    print()
def User_status():
    c_k=input("Enter user to check: ")
    if c_k in list(d.keys()):
        print(f'user "{c_k}" exists')
    else:
        print(f'user "{c_k}" not found in the chat')
    print()
def commonly_repeated_words():
    from collections import Counter
    u=" ".join(d1)
    r=dict(Counter(u.split()))
    s1={}
    for i in r:
        if r[i]>1:                                      #max(r.values())
            s1[i]=r[i]                                  #s1[i]=max(r.values())
    print(s1)
    print(f'Common repeated words are {sorted(s1.keys(),key=s1.get,reverse=True)}')
    print()
def longest_avg_msg_lenght_user():
    o={}
    for i,j in d.items():
        o.update({i:(len((' '.join(d[i]).split()))/len(j))})
    v=sorted(o, key=o.get,reverse=True)
    print(f'The user with the longest average message length: {v[0]}',end=":")
    for i,j in o.items():
        if i==v[0]:
            print(j)
    print()
def msgs_mentioned_user():
    s_c=input("Enter user name to search: ")
    if s_c in ' '.join(d1):
        print(f'The times {s_c} mentioned is {" ".join(d1).count(s_c)}')
    else:
        print(f'The times {s_c} mentioned is 0')
    print()
def Remove_duplicate_messages():
    x=[]
    for i in d1:
        if d1.count(i)>1:
            if i not in x:
                x.append(f'{i}')
    if len(set(d1))!=len(d1):
        print(f'Unique messages count:{len(s)}')
        print(f'Duplicate messages:{x}')
    else:
        print(f'Unique messages count:{l}')
        print(f'No Duplicates Found')
    print()
def Sort_msgs():
    print(f'Sorted Messages:{sorted(d1)}')
    print()
def Questions_chat():
    for i in d1:
        if '?' in i:
            print(i)
    else:
        print("No Questions Asked in the chat")
    print()
def reply_ratio():
    nm1,nm2=input("Enter users for reply ratio with space seperated: ").split()
    x=0
    for i,j in d.items():
        if i==nm2:
            x=' '.join(d[nm2]).count(nm1)
    print(f'Reply ratio from {nm2} to {nm1}:{x} replies')
    print()
def Deleted_msgs_count():
    count1=0
    for i in d1:
        if i=='This message was deleted':
            count1+=1
    print(f'Deleted messages found:{count1}')
    print()
    
while True:
    print('0.Exit')
    print('1.Total number of messages')
    print('2.Unique users in the chat')
    print('3.Total words in the chat')
    print('4.Average words per message')
    print('5.Longest message sent')
    print('6.The Most active user')
    print('7.Message count for a specific user')
    print('8.The Most frequently used word by a specific user')
    print('9.Retrieve the first and last message sent by a user')
    print('10.Check if a user is present in the chat')
    print('11.Find commonly repeated words')
    print('12.The user with the longest average message length')
    print('13.Count how many messages mention a specific user')
    print('14.Remove duplicate messages')
    print('15.Sort Messages Alphabetically ')
    print('16.Extract All questions in the chat')
    print('17.Calculate the reply ratio b/w two users')
    print('18.Check for deleted messages and its count')
    
    ch=int(input('Enter your chioice: '))
    if ch==0:
          break
    elif ch==1:
          Total_messages()
    elif ch==2:
          Unique_Users()
    elif ch==3:
          Total_Words()
    elif ch==4:
          Average_Words_Per_Message()
    elif ch==5:
          Longest_Message()
    elif ch==6:
          Most_active_user()
    elif ch==7:
          Message_count_user()
    elif ch==8:
          Most_frequent_word_user()
    elif ch==9:
          First_Last_msg_user()
    elif ch==10:
          User_status()
    elif ch==11:
          commonly_repeated_words()
    elif ch==12:
          longest_avg_msg_lenght_user()
    elif ch==13:
          msgs_mentioned_user()
    elif ch==14:
          Remove_duplicate_messages()
    elif ch==15:
          Sort_msgs()
    elif ch==16:
          Questions_chat()
    elif ch==17:
          reply_ratio()
    elif ch==18:
          Deleted_msgs_count()
    else:
        print("Invalid Choice")
        print("Try Again!")
        print()
