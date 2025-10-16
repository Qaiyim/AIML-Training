def add(num1,num2):
    return num1+num2

def multi(num1,num2):
    return num1*num2

def avg(num1,num2):
    return (num1+num2)/2

def sub(num1,num2):
    return num1-num2

def div(num1,num2):
    return num1/num2

print('Welcome to our calculator')
while True:
    print('Select Operation \n1.Add \n2.Sub \n3.Multi \n4.Division \n5.Average \n6.Exit')
    operation=int(input('Enter your operation choice (1-6):\t'))
    if(operation==6):
        print('Goodbye Bestie')
        break
    if((operation>=6) or (operation<=0)):
        print('Wrong operation choice,only 1 to 6 are allowed')
        break
    fnum=float(input('Enter first number:\t'))
    snum=float(input('Enter second number:\t'))
    if(operation==1):
        print(f'Result after adding {fnum},{snum}:\t',add(fnum,snum))
    elif(operation==2):
        print(f'Result after subtracting {snum} from {fnum}:\t', sub(fnum,snum))
    elif(operation==3):
        print(f'Result after multiplying {fnum} and {snum}:\t', multi(fnum,snum))
    elif(operation==4):
        print(f'Result after dividing {fnum} by {snum}:\t', div(fnum,snum))
    elif(operation==5):
        print(f'Average of {fnum} and {snum}\t', avg(fnum,snum))
    else:
        print('Wrong operation choice, please choose only 1 to 6')





