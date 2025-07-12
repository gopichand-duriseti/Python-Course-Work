'''
bullets=10
while bullets>0:
    if bullets==5:
        print('Dead')
        break
    print(f'Bullets are left-You can shoot()')
    bullets-=1
else:
    print("Game over")

#PRIME NUMBERS
fact=0
n=int(input('Enter n:'))
for i in range(2,(n//2)+1):
    if n%i==0:
        fact+=1
if fact==0:
    print(f'{n} is prime number\nFactors count={fact}')
else:
    print(f'{n} is not prime number\nFactors count={fact}')
'''





