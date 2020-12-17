class MyException(Exception):
    pass

class MySubException(MyException):
    pass

import sys

a = int(input('Give me a:'))
b = 15
try:
    #c = a * d
    c = a + b
    print('c:')
    sys.stderr.write('am writing to error\n')
    print(c)
    if c > 20:
        raise MySubException('C > 20')
    if c > 25:
        raise MyException('Error in c')
except MySubException as ne:
    print(type(ne))
    print('My SUB exception occured: ' + str(ne))
    exit('Error in this code')
except MyException as ne:
    print(type(ne))
    print('My exception occured: ' + str(ne))
except Exception as e:
    print(type(e))
    print('exception occured: ' + str(e))
print('continuing....')

#except NameError as ne:
#    print('exception occured: ' + str(ne))
