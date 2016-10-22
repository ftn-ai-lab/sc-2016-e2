 
 
class Greeter(object):
	def __init__(self, name):
		self.name = name
		
	def greet(self, loud=False):
		if loud:
			print 'Hello '+self.name.upper()
		else:
			print 'Hello '+self.name

g = Greeter('Fred')
g.greet()
g.greet(loud=True)