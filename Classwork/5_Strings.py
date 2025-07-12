print('''1)Case Conversion Methods''')
name='gopi is a good guy'
print(name) #gopi is a good guy
print('name.upper():',name.upper()) #name.upper(): GOPI IS A GOOD GUY
name='siddu is also a good guy'
print('name.lower():',name.lower()) #name.lower(): siddu is also a good guy
s='I am a student'
print('s.capitalize():',s.capitalize()) #s.capitalize(): I am a student
t='python is a good subject'
print('t.title():',t.title()) #t.title(): Python Is A Good Subject
sw="dO yoU KnOw mE?"
print('sw.swapcase():',sw.swapcase()) #sw.swapcase(): Do YOu kNoW Me?
c="ß"
print('c.casefold():',c.casefold()) #c.casefold(): ss
print()
print('''2)Alignment & Formatting Methods''')
name='Alignment & Formatting Methods'
print(name) #Alignment & Formatting Methods
cen=name.center(50,'^')
print('cen:',cen) #cen: ^^^^^^^^^^Alignment & Formatting Methods^^^^^^^^^^
ljus=name.ljust(50,'.')
print('ljus:',ljus) #ljus: Alignment & Formatting Methods....................
print('Name'.ljust(50,' ') + ':') ##Name                                              :
zfil='56'.zfill(5) 
print('zfil:',zfil) #zfil: 00056
print(''.zfill(10)) #0000000000
print()
print('''3)Search & Find Methods''')
name='Tarak is good boy'
print(name)
print('find(mohit):',name.find('mohit')) #find(mohit): -1
print("rfind('a'):",name.rfind('a')) #rfind('a'): 3
print("rindex('a'):",name.rindex('a')) #rindex('a'): 3
print()
print('''4)String Testing Methods (Boolean Results)''')
print("PFS30.startswith('PFS'):",'PFS30'.startswith('PFS')) #PFS30.startswith('PFS'): True
print("PFS30.endswith('30'):",'PFS30'.endswith('30')) #PFS30.endswith('30'): True
print("PFS30.isalpha():",'PFS30'.isalpha()) #SIMILARLY ISDIGIT() #PFS30.isalpha(): False
print("arun123.isalnum():",'arun123'.isalnum()) #arun123.isalnum(): True
print("'gopi'.islower():","gopi".islower()) #'gopi'.islower(): True
print("'GOPI'.isupper():",'GOPI'.isupper()) #'GOPI'.isupper(): True
print("' '.isspace():",' '.isspace()) #' '.isspace(): True
print("'I Am Fine'.istitle():",'I Am Fine'.istitle()) #'I Am Fine'.istitle(): True
print()
print('''5)Replace & Modify Methods''')
name='He is a good student'
print(name)
print("name.replace('is','was'):",name.replace('is','was')) #name.replace('is','was'): He was a good student
print("name.translate(str.maketrans('agou','zy%6')):",name.translate(str.maketrans('agou','zy%6'))) #name.translate(str.maketrans('agou','zy%6')): He is z y%%d st6dent
print()
print('''6)Splitting & Joining Methods''')
name="Hello! How are you?"
print(name)
print("name.split(' '):",name.split(' ')) #name.split(' '): ['Hello!', 'How', 'are', 'you?']
print("name.split('o'):",name.split('o')) #name.split('o'): ['Hell', '! H', 'w are y', 'u?']
print("name.rsplit(' ',2):",name.rsplit(' ',2)) #name.rsplit(' ',2): ['Hello! How', 'are', 'you?']
name='''hello\nsirrrrrrrrr'''
print('name.splitlines():',name.splitlines()) #name.splitlines(): ['hello','sirrrrrrrrr']
l=['1','2','3','4']
print('"".join(l):',"".join(l))
s='Hello,welcome,everyone'
print("s.partition(','):",s.partition(',')) #s.partition(','): ('Hello', ',', 'welcome,everyone') #left /first comma will occur in list
print("s.rpartition(','):",s.rpartition(',')) #s.rpartition(','): ('Hello,welcome', ',', 'everyone') #right/last comma will occur in list
print()
print('''7)Whitespace & Trimming Methods''')
s='      Hello     '
print("s.strip():",s.strip()) #s.strip(): Hello #Strip and lstrip looks almost same
print("s.rstrip():",s.rstrip()) #s.rstrip():       Hello
print()
print('''8)Encoding & Decoding Methods''')
text="Hello नमते你好 café 🙂"
print("text.encode():",text.encode('utf-8')) #text.encode(): b'Hello \xe0\xa4\xa8\xe0\xa4\xae\xe0\xa4\xa4\xe0\xa5\x87\xe4\xbd\xa0\xe5\xa5\xbd caf\xc3\xa9 \xf0\x9f\x99\x82'
byt=b'Hello \xe0\xa4\xa8\xe0\xa4\xae\xe0\xa4\xa4\xe0\xa5\x87\xe4\xbd\xa0\xe5\xa5\xbd caf\xc3\xa9 \xf0\x9f\x99\x82'
print("byt.decode('utf-8'):",byt.decode('utf-8')) #byt.decode('utf-8'): Hello नमते你好 café 🙂
