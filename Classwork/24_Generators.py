def feed(l):
    yield l
l=['1..100','101..200','201..300','300..400'] 
print(feed(l)) #<generator object feed at 0x000001780EE05E40>
#To watch the items/elements in the list
load=feed(l)
print(next(load)) #['1..100', '101..200', '201..300', '300..400'] #Insta Reels

def feed(l):
   for i in l:
      yield i 
l=['1..100','101..200','201..300','300..400'] 
print(feed(l)) #<generator object feed at 0x000001780EE05E40>
#To watch the items/elements in the list
load=feed(l)
print(next(load)) #1..100
print(next(load)) #101..200
print(next(load)) #201..300
print(next(load)) #300..400
#print(next(load)) #Error:StopIteration

def feed(l):
   for i in l:
      yield i 
l=['file1','file2','file3','file4'] 
load=feed(l)
print(next(load)) 
print(next(load)) 
print(next(load)) 
print(next(load)) 


def square_numbers(n):
    for i in range(n):
        yield i * i
squares = square_numbers(5)
print(next(squares)) # Output: 0
print(next(squares)) # Output: 1




'''def movies(mov):
    for i in mov:
        yield i
mov=['Bahubali2','Hit3','Jersey','Janagana Mana','Racegurram']        
load=movies(mov)
x=next(load)
def opt(options):
    for _ in mov:
        o=input('Enter Option: ')
        if o=='play':
            print(f'{x} movie playing')
        elif o=='next':
            print(next(load))
load1=opt(['play','pause','next'])'''

def movies(mov):
    for i in mov:
        yield i

mov = ['Bahubali2', 'Hit3', 'Jersey', 'Janagana Mana', 'Racegurram']
load = movies(mov)
import time
def opt():
    current = None
    while True:
        print("\n🎬 Movie Player Options:")
        print("1. play  → Play current movie")
        print("2. next  → Move to next movie")
        print("3. exit  → Exit the player\n")
        o = int(input("Enter your choice: "))
        if o == 1:
            if current:
                print(f'{current} movie playing')
            else:
                print("No movie selected. Use 'next' to choose a movie.")
        elif o == 2:
            try:
                current = next(load)
                print(f'{current} is playing now')
            except StopIteration:
                print("No more movies left.")
                break
        elif o == 3:
            print("Exiting...")
            time.sleep(30)
            break
        else:
            print("Unknown option. Use 'play', 'next', or 'exit'.")
opt()
     

def songs(son):
    for i in son:
        yield i
son=['Saiyaara','Anna Antene','Sapphire','Poraatame','Naatu Naatu','Peelings']
load1=songs(son)
def option():
    current_m=None
    while True:
        o=input('Enter the choice: ')  
        if o=='play':
            if current_m:
                print(f'{current_m} is playing')
            else:
                print('No song is playing,Select "next" to play a song')
        elif o=='next':
            try:
                current_m=next(load1)
                print(f'{current_m} is playing now')
            except StopIteration:
                print("No songs left")
        else:
            print('Exiting')
            break
option()
        

         
