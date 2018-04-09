from random import shuffle
import os

def generar_lista_jugador(numero):
	preferencias = [i+1 for i in range(20)]
	shuffle(preferencias)
	with open('galeshapley_test_files/jugador_' + numero +'.csv', 'w') as f:
		f.write(preferencias[0].__str__())
		for x in preferencias[1:]:
			f.write(',' + x.__str__())
	print('Jugador ', numero, ' OK.')
	
def generar_lista_equipo(numero):
	preferencias = [i+1 for i in range(200)]
	shuffle(preferencias)
	with open('galeshapley_test_files/equipo_' + numero +'.csv', 'w') as f:
		f.write(preferencias[0].__str__())
		for x in preferencias[1:]:
			f.write(',' + x.__str__())
	print('Equipo ', numero, ' OK.')

if not os.path.exists('galeshapley_test_files'):
    os.makedirs('galeshapley_test_files')
for i in range(200):
	generar_lista_jugador((i+1).__str__())

for i in range(20):
	generar_lista_equipo((i+1).__str__())
