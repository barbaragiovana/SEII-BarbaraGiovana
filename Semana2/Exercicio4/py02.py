print('Hello World')

message = 'Hello World'
print(message)

message = 'Bobby\'s World'
message = "Bobby's World"
message = """Bobby's World was a good
cartton in the 1990s"""

message = 'Hello World'
print(len(message))
print(message[0])
print(message[10])
print(message[0:5])
print(message[:5])
print(message[6:])
print(message.lower())
print(message.upper())
print(message.count('Hello'))
print(message.count('l'))
print(message.find('World'))
print(message.find('Universe'))

new_message = message.replace('World', 'Universe')
print(new_message)

gretting = 'Hello'
name = 'Michael'
message = gretting + name
print(message)
message = gretting + ', ' + name
print(message)
message = gretting + ', ' + name + '. Welcome!'
print(message)
message = '{}, {}. Welcome!'.format(gretting, name)
print(message)
message = f'{gretting}, {name}. Welcome!'
print(message)
message = f'{gretting}, {name.upper()}. Welcome!'
print(message)

print(dir(name))

print(help(str))

print(help(str.lower))
