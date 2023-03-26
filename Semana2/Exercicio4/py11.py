f = open("test.txt", "r")
# f = open("test.txt", "w")
# f = open("test.txt", "a")
# f = open("test.txt", "r+")
print(f.name)
print(f.mode)
f.close()

with open("test.txt", "r") as f:
  f_contents = f.read()
  print(f_contents)

with open("test.txt", "r") as f:
  f_contents = f.readlines()
  print(f_contents)

with open("test.txt", "r") as f:
  f_contents = f.readlines()
  print(f_contents)

with open("test.txt", "r") as f:
  f_contents = f.readline()
  print(f_contents)
  f_contents = f.readline()
  print(f_contents)

with open("test.txt", "r") as f:
	f_contents = f.readline()
	print(f_contents, end = '')
	f_contents = f.readline()
	print(f_contents, end = '')

with open("test.txt", "r") as f:
  for line in f:
	  print(line, end = '')
	
with open("test.txt", "r") as f:
	f_contents = f.read(100)
	print(f_contents, end = '')
	f_contents = f.read(100)
	print(f_contents, end = '')
	f_contents = f.read(100)
	print(f_contents, end = '')

with open("test.txt", "r") as f:
	size_to_read = 100
	f_contents = f.read(size_to_read)
	while len(f_contents) > 0:
		print(f_contents)
		f_contents = f.read(size_to_read)

with open("test.txt", "r") as f:
	size_to_read = 10
	f_contents = f.read(size_to_read)
	print(f_contents, end = '')
	f.seek(0)
	f_contents = f.read(size_to_read)
	print(f_contents, end = '')
	print(f.tell())
	while len(f_contents) > 0:
		print(f_contents, end = '*')
		f_contents = f.read(size_to_read)

with open("test2.txt", "w") as f:
	pass
	f.write("Test")
	f.seek(0)
	f.write("Test")
	f.seek("R")

with open("test.txt", "r") as rf:
	with open("test_copy.txt", "w") as wf:
		for line in rf:
			wf.write(line)
