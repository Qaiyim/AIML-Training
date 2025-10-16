#write a function to find out the table of given number
def gen_table(num):
    for i in range(1,11):
        print(f'{num}*{i}=\t{(num*1)}')

number=int(input('Enter number to findout table:\t'))
gen_table(number)