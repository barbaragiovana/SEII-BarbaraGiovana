import os

os.chdir('/mnt/d/www/ufu/s7/SEII-MatheusMenezesPedrosa/Semana02/Exercicio04')
print(os.getcwd())

for f in os.listdir():
  print(f)

for f in os.listdir():
  print(os.path.splitext(f))

for f in os.listdir():
  f_name, f_ext = os.path.splitext(f)

  f_title, f_course, f_number = f_name.split('-')

  f_title = f_title.strip()
  f_course = f_course.strip()
  f_number = f_number.strip()[1:].zfill(2)

  print('{}-{}{}'.format(f_number, f_title.strip(), f_ext.strip()))

  new_name = '{}-{}{}'.format(f_number, f_title, f_ext)

  os.rename(f, new_name)
