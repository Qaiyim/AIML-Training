import random
def findwinner():
    name=input('Enter your name:\t')
    luckynumber=random.randint(1,10)
    print(f'Welcome Mr.\\Ms. {name} Coupon Number: {luckynumber}')
    if(luckynumber==1):
        print(f'Mr.\\Ms. {name} you have won Nissan R35')
    elif(luckynumber==3):
        print('You have won a jet to holiday')
    elif(luckynumber==39):
        print('You have won a Y15zr')
    else:
        print('Better Luck Next Time')
