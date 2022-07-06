# Los bloques en las sentencias condicionales se definen por la identación, es 
# decir tenemos que dejar un sangrado parar indicar el código dentro del la 
# condicional

#--------------#
# Sentencia IF #
#--------------#
a = 5
b = 4
c = 6
print('\nSentencia IF')
if (a > b):
	print('El código se ejecuta dentro del IF')
print('Este código se ejecutara siempre')

#---------------------#
# Sentencia IF...ELSE #
#---------------------#
print('\nSentencia IF...ELSE')
if (a > b):
	print('A > B')
else:
	print('B > A')

#----------------#
# Sentencia elif #
#----------------#
print('\nSentencia ELIF')
if (a > b):
	print('A > B')
elif (a > c):
	print('A > C')
else:
	print('A no es el mayor')