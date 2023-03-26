try:
  f = open('test_file.txt')
except Exception:
  print('Sorry. This file does not exist')

try:
  f = open('test_file.txt')
except FileNotFoundError:
  print('Sorry. This file does not exist')
except Exception:
  print('Sorry. Something went wrong')

try:
  f = open('test_file.txt')
except FileNotFoundError as e:
  print(e)
except Exception as e:
  print(e)
else:
  print(f.read())
  f.close()

try:
  f = open('test_file.txt')
except FileNotFoundError as e:
  print(e)
except Exception as e:
  print(e)
else:
  print(f.read())
  f.close()
finally:
  print("Executing Finally...")

try:
  f = open('corrupt_file.txt')
  if f.name == 'corrupt_file.txt':
    raise Exception
except FileNotFoundError as e:
  print(e)
except Exception as e:
  print('Error!')
else:
  print(f.read())
  f.close()
finally:
  print("Executing Finally...")

try:
  f = open('corrupt_file.txt')
  #if f.name == 'corrupt_file.txt':
    #raise Exception
except FileNotFoundError as e:
  print(e)
except Exception as e:
  print('Error!')
else:
  print(f.read())
  f.close()
finally:
  print("Executing Finally...")
