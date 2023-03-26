language = 'Python'
if language == 'Python':
	print('Conditional was True')

if language == 'Python':
	print('Language is Python')
else:
	print('No match')

language = 'Java'
if language == 'Python':
	print('Language is Python')
else:
	print('No match')
if language == 'Python':
	print('Language is Python')
elif language == 'Java':
	print('Language is Java')
else:
	print('No match')

if language == 'Python':
	print('Language is Python')
elif language == 'Java':
	print('Language is Java')
elif language == 'JavaScript':
	print('Language is JavaScript')
else:
	print('No match')

user = 'Admin'
logged_in = True
if user == 'Admin' and logged_in:
	print('Admin Page')
else:
	print('Bad Creds')

logged_in = False
if user == 'Admin' and logged_in:
	print('Admin Page')
else:
	print('Bad Creds')

if user == 'Admin' or logged_in:
	print('Admin Page')
else:
	print('Bad Creds')

if not logged_in:
	print('Please Log In')
else:
	print('Welcome')

a = [1,2,3]
b = [1,2,3]
print(a==b)
print(a is b)
print(id(a))
print(id(b))
print(a==b)

a = [1,2,3]
b = a
print(id(a))
print(id(b))
print(id(a) == id(b))

condition = False
if condition:
	print('Evalued to True')
else:
	print('Evalued to False')

condition = None
if condition:
	print('Evalued to True')
else:
	print('Evalued to False')

condition = 10
if condition:
	print('Evalued to True')
else:
	print('Evalued to False')

condition = []
if condition:
	print('Evalued to True')
else:
	print('Evalued to False')

condition = ''
if condition:
	print('Evalued to True')
else:
	print('Evalued to False')

condition = 'Test'
if condition:
	print('Evalued to True')
else:
	print('Evalued to False')
