x=3
print type(x) # <type 'int'>

print x + 1
print x - 1
print x * 2
print x ** 2

x+=1
print x

x *= 2
print x

y = 2.5
print type(y) # prints <type 'float'>
print y, y+1, y*2, y**2


t = True
f = False

print t and f # AND
print t or f  # OR
print not t   # not
print t != f  # XOR

hello = 'Hello'
world = "world"
print hello
print len(hello)
hw = hello + ' '+ world
print hw
hw12 = '%s %s %d'%(hello, world, 12)
print hw12

s = "hello"

print s.capitalize()
print s.upper()
print s.rjust(7)
print s.center(7)
print s.replace('l', '(ell)')
print '   world  '.strip()









