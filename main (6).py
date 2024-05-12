def ExD(n):
  if n == 1:
      return 1
  else:
      return n**2 * ExD(n - 1) + n - 1

resultado = ExD(2)
print(resultado)  
