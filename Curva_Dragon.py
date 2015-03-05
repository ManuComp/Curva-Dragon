def curva(n):
  if n == 0:
    return []
  else:
    c = curva(n - 1)
    r = c[::-1]
    i = ['I' if g == 'D' else 'D' for g in r]
    return c + ['I'] + i

pregunta = "Que numero de iteracion queire saber: "
print(pregunta)
x = input()
for i in range(x):
      print('orden {0}: {1}'.format(i, ''.join(curva(i))))
