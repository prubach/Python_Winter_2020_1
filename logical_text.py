#p = True
p = bool('true')
q = False
r = p and q
s = p or (q and r)

print(r)
print(s)

print(type(s))
print(type(bool('true')))

ttt = 'abc\tdef\nefg'
print(ttt)

ttt = 'abcd\tdef\nefg'
print(ttt)

ttt = 'abcde\tdef\nefg'
print(ttt)

ttt = 'abcdef\tdef\nefg'
print(ttt)
