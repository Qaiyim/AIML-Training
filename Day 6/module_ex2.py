# import datetime
# import inspect

# print('Today is Date: ',datetime.date.today())

# datetimeclasses=inspect.getmembers(datetime,inspect.isclass)
# print('All classes inside datetime module')

# for n,func in datetimeclasses:
#     print(n)

# print('All functions inside datetime.date class')

# functions=inspect.getmembers(datetime.date,inspect.isbuiltin)
# for n,func in functions:
#     print(n)

# import os
# import inspect
# functions=inspect.getmembers(os,inspect.isbuiltin)
# for n,func in functions:
#     print(n)

# listDirs=os.listdir()

import os
dirs=os.listdir()
for dr in dirs:
    print (dr)