# BackEnd

## Objetivos
- *Entender la sintaxis de Python*
- *Declarar variables en Python*

## Guía de estilo para Python
- [IDENTACION](https://peps.python.org/pep-0008/#indentation):
Utilice 4 espacios por cada identación

```
# Alinear con el delimitador de inicio de apertura
foo = long_function_name(var_one, var_two, 
												 var_three, var_four)


# Alineacion con estamentos condicionales
if (this_is_one_thing 
			and that_is_another_thing):
		do_something()
```

- [TAMAÑO MAXIMO LINEA](https://peps.python.org/pep-0008/#maximum-line-length): 
Limite todas las lineas a un máximo de 79 caracteres. Para documentaciones y 
comentarios limite la cantidad de caracteres a 72.

- [SALTO DE LINEA AL USAR OPERADORES BINARIOS](https://peps.python.org/pep-0008/#should-a-line-break-before-or-after-a-binary-operator)
```
# Forma correcta de conectar operadores con sus operandos
income = (var_one
					+ var_two
					+ (var_three - var_four)
					- var_five
					- var_six)
```

- [IMPORTACIONES](https://peps.python.org/pep-0008/#imports)
```
# Las importaciones se deben realizar de forma separada
import os
import sys

# Tambien es correcto
from subprocess import Popen, PIPE
```

- [ESPACIO EN BLANCO EN LAS EXPRESIONES Y ESTAMENTOS](https://peps.python.org/pep-0008/#whitespace-in-expressions-and-statements)
	- *Utilizando parentesis*
	```
		spam(ham[1], {eggs: 2})
	```
	- *Después de una coma y entre parentesis*
	```
		foo = (0,)
	```

	- *Inmediamente antes de una coma, punto y coma*
	```
		if x == 4: print(x, y); x, y = y, x
	```
	- *Alineando operadores*
	```
		x 						= 1
		y 						= 2
		long_variable = 3
	```
	- *Utilizando operadores con diferentes prioridades*
	```
		i = i + 1
		x = x*2 - 1
		hypot = x*x + y*y
		c = (a+b) * (a-b)
	```

- [COMENTARIOS](https://peps.python.org/pep-0008/#comments)
- [CONVENCIÓN NOMBRES](https://peps.python.org/pep-0008/#naming-conventions)