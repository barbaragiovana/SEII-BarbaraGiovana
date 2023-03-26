for a in range(2):
  x = 'global {}'.format(a)


def outer():
  for b in range(3):
    x = 'outer {}'.format(b)

  def inner():
    for c in range(4):
      x = 'inner {}'.format(c)
    print(x)
    print(a, b, c)

  inner()
  print(x)
  print(a, b)

outer()
print(x)
print(a)
