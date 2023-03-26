import os
from datetime import datetime

print(dir(os))
print(os.getcwd())

os.chdir('/mnt/d/www/ufu/s7/SEII-MatheusMenezesPedrosa/Semana02/')
print(os.getcwd())

print(os.listdir())

os.mkdir('os-module')
os.makedirs('os/getcwd')
print(os.listdir())

os.rmdir('os-module')
os.removedirs('os/getcwd')
print(os.listdir())


os.mkdir('os-module')
os.rename('os-module', 'os-demo')
print(os.listdir())

os.rmdir('os-demo')

print(os.stat('exercicio02.txt'))
print(os.stat('exercicio02.txt').st_size)
print(os.stat('exercicio02.txt').st_mtime)

mod_time = os.stat('exercicio02.txt').st_mtime
print(datetime.fromtimestamp(mod_time))

for dirpath, dirnames, filenames in os.walk('/mnt/d/www/ufu/s7/SEII-MatheusMenezesPedrosa/Semana02/'):
  print('Current Path:', dirpath)
  print('Directories:', dirnames)
  print('Files:', filenames)

print(os.environ.get('HOME'))

file_path = os.path.join(os.environ.get('HOME'), 'test.txt')
print(file_path)

print(os.path.basename('/tmp/test.txt'))
print(os.path.dirname('/tmp/test.txt'))
print(os.path.split('/tmp/test.txt'))
print(os.path.exists('/tmp/test.txt'))
print(os.path.isdir('/tmp/test.txt'))
print(os.path.isfile('/tmp/test.txt'))
print(os.path.splitext('/tmp/test.txt'))

print(dir(os.path))
