d = {'cat': 'cute', 'dog': 'furry'}
print d['cat']

print 'cat' in d

d['fish'] = 'wet'
print d

print d.get('monkey', 'n/a')
del d['fish']

d = {'person': 2, 'cat':4, 'spider': 8}
for animal in d:
	print animal, d[animal]

