#p = True
p = bool('true')
s = 'abc"'
s = "abc\"'"
print(s)
print(s[2:])
print(s[:4])
print(s[2:4])
print(s[-3:])
#p = False
"""
q = False

"""

q = False
p = False
a = 50
if p:
    b = 60
    print('p is true')
    print('only of p is true')
    print('a=' + str(a))
    print('b=' + str(b))
else:
    b = 80
    print('p is not true')
    print('a=' + str(a))

#print('only if not p')
print('after the block')
print('a=' + str(a))
print('b=' + str(b))


def my_func(u):
    i = 78
    print('running function u=' + str(u))
    print('running function i=' + str(i))


def add(a, b):
    return a + b

i = 60
my_func(20)
for j in range(2):
    for i in range(3):
        print('i=' + str(i))
    print('finished j loop for j=' + str(j))

print('after the loop')
my_func(20)
print('i=' + str(i))

print(add(5, 10))


