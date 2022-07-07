#-----------------#
# Sentencia WHILE #
#-----------------#
print('Sentencia WHILE')
i = 1
while i < 6:
	print(i)
	i += 1


print('Sentencia WHILE con BREAK')
i 					= 1
while_break = False
while i < 6:
	if i == 3:
		print(not while_break)
		break
	print(while_break)
	i += 1

print('Sentencia WHILE con CONTINUE')
i 						 = 0
while_continue = False
while i < 6:
	i += 1
	if i == 3:
		print('No se realiza nada')
		continue
	print(i)
	print('->')