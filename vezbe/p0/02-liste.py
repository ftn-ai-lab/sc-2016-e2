xs = [3, 1, 2]

print xs, xs[2]
print xs[-1]

xs[2] = 'foo'
print xs

xs.append('bar')
print xs

x = xs.pop()
print x, xs

nums = range(5)
print nums

print nums[2:4]
print nums[2:]
print nums[:2]
print nums[:-1]

nums[2:4] = [8, 9]
print nums


animals = ['cat', 'dog', 'monkey']
for animal in animals:
	print animal
	
animals = ['cat', 'dog', 'monkey']
for idx, animal in enumerate(animals):
		print idx, animal
		
nums = [0, 1, 2, 3, 4]
squares = []
for x in nums:
	squares.append(x ** 2)
	
print squares	

		
		
nums = [0, 1, 2, 3, 4]
squares = [x ** 2 for x in nums]
print squares
	

nums = [0, 1, 2, 3, 4]
squares = [x ** 2 for x in nums if x%2==0]
print squares
	
	
	



	