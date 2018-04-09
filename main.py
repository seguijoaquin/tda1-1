import numpy

from graficador import *
from quicksort import quicksort
from merge import merge_sort
from insercion import insercion
from seleccion import seleccion

algoritmos = {
	'Quicksort' : quicksort,
	'Mergesort' : merge_sort,
	'Insercion' : insercion,
	'Seleccion' : seleccion
}

set_lengths = [50,100,500,1000,2000,3000,4000,5000,7500,10000]

def calcular_tiempos_algoritmo(sets,algoritmo):
	results = {}
	for set_length in set_lengths:
		results[set_length] = []
	for set_length in set_lengths:
		log('Aplicando a set de {} elementos.'.format(set_length))
		for set in sets:
			vector = set[:set_length]
			tiempo = performance(vector,algoritmo)
			results[set_length].append(tiempo)
	return results

def calcular_tiempos_ejecucion(sets):
	results = {}
	for clave in algoritmos:
		algoritmo = algoritmos[clave]
		log('Calculando tiempos ejecucion de {}.'.format(clave))
		tiempos = calcular_tiempos_algoritmo(sets,algoritmo)
		results[clave] = tiempos
	return results

def calcular_tiempos_medios(tiempos_ejecucion):
	tiempos_medios = {}
	for key,value in enumerate(tiempos_ejecucion):
		tiempos_medios[value] = {}
		for key_set,set_length_value in enumerate(set_lengths):
			log('Calculando tiempo medio de {} para {} elementos.'.format(value,set_length_value))
			tiempos_medios[value][set_length_value] = numpy.mean(tiempos_ejecucion[value][set_length_value])
	
	return tiempos_medios

def mostrar_resultados(tiempos_medios):
	for algoritmo in tiempos_medios:
		log('Algoritmo: {}'.format(algoritmo))
		for set_length in set_lengths:
			log('{0:10},{1:10f}'.format(set_length,tiempos_medios[algoritmo][set_length]))

def graficar(tiempos_medios):
	elementos = []
	tiempo = []
	for i in tiempos_medios:
#		for j in tiempos_medios[i]:
#			elementos.append(j)
#			tiempo.append(tiempos_medios[i][j])
		fig, ax = plt.subplots(1,1, figsize=(8, 6))
		ax.plot(*zip(*sorted(tiempos_medios[i].items())))
#		ax.plot([j for j in tiempos_medios[i]], [tiempos_medios[i][j] for j in tiempos_medios[i]])
		fig.suptitle(i, fontsize=16)
		plt.xlabel('Elementos [un]', fontsize=12)
		plt.ylabel('Tiempo [seg]', fontsize=12)
		fig.savefig(i + '.png')
		elementos = []
		tiempo = []


def correr_tp():
	log('Construyendo sets de numeros aleatorios..')
	sets = []
	for i in enumerate(set_lengths):
		sets.append(gen_vector(10000))

	log('Calculando tiempos de ejecucion para cada set..')
	tiempos_ejecucion = calcular_tiempos_ejecucion(sets)

	log('Estimando tiempo medio de cada algoritmo..')
	tiempos_medios = calcular_tiempos_medios(tiempos_ejecucion)

	log('Resultados:')
	mostrar_resultados(tiempos_medios)

	log('Graficando Resultados:')
	graficar(tiempos_medios)

if __name__ == '__main__':
	correr_tp()
