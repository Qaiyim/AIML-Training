import datetime
import inspect
dtclasses= inspect.getmembers(datetime,inspect.isbuiltin)

print('All classes in datetime module')
for n,func in dtclasses:
    print(n,end='\t')

print('\n---Today---\n')
print(datetime.date.today())

print('\n---Current Date Time---\n')
print(datetime.datetime.now())
print('\n---Current Time---\n')
print(datetime.datetime.now().time())
print(datetime.datetime.now().time())

cttime=datetime.datetime.now().time()
formatedtime=datetime.datetime.now().strftime('%I:%M:%S:%p')

print('Current Time',cttime)
print('Formated Time',formatedtime)

