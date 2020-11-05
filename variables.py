a = 50

b = 'abc' + '45'

print(b)

print(b.isalnum())
print(b.index('c'))


def index(needle, stack):
    return stack.index(needle)


print('found: ')
print(index('bc', b))


