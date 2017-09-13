
<<<<<<< HEAD
Import jogovelha
import sys

erroInicializar = False
jogo = jogovelha.inicializar()

if len(jogo) != 3:
	erroInicializar = True
else:
	for linha in jogo:
		if len(linha) != 3:
			erroInicializar = True
	else:
	for elemento in linha:
		if elemento != '.':
			erroInicializar = True
if erroInicializar:
	sys.exit(1)
else:
	sys.exit(0)
=======
>>>>>>> 04bd3dda61451b938dbc616a0766bda3975941d0
