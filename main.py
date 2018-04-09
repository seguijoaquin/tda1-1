import numpy

import logging
FORMAT = "%(asctime)-15s    %(sort)-8s     %(message)s"
logging.basicConfig(format=FORMAT,filename='main.log', level=logging.INFO)

from graficador import *
from quicksort import quicksort
from merge import merge_sort
from insercion import insercion
from seleccion import seleccion

algoritmos = {
	'quicksort' : quicksort,
	'mergesort' : merge_sort,
	'insercion' : insercion,
	'seleccion' : seleccion
}

set_lengths = [50,100,500,1000,2000,3000,4000,5000,7500,10000]

def calcular_tiempos_algoritmo(sets,algoritmo):
	results = {}
	for set_length in set_lengths:
		results[set_length] = []
	for set_length in set_lengths:
		print('Aplicando a set de {} elementos.'.format(set_length))
		logging.debug('Aplicando a set de {} elementos.'.format(set_length))
		for set in sets:
			vector = set[:set_length]
			tiempo = performance(vector,algoritmo)
			results[set_length].append(tiempo)
	return results

def calcular_tiempos_ejecucion(sets):
	results = {}
	for clave in algoritmos:
		algoritmo = algoritmos[clave]
		print('Calculando tiempos ejecucion de {}.'.format(clave))
		logging.debug('Calculando tiempos de ejecucion de {}.'.format(clave))
		tiempos = calcular_tiempos_algoritmo(sets,algoritmo)
		results[clave] = tiempos
	return results

def calcular_tiempos_medios(tiempos_ejecucion):
	tiempos_medios = {}
	for key,value in enumerate(tiempos_ejecucion):
		tiempos_medios[value] = {}
		for key_set,set_length_value in enumerate(set_lengths):
			print('Calculando tiempo medio de {} para {} elementos.'.format(value,set_length_value))
			tiempos_medios[value][set_length_value] = numpy.mean(tiempos_ejecucion[value][set_length_value])
	
	return tiempos_medios

def mostrar_resultados(tiempos_medios):
	for algoritmo in tiempos_medios:
		print algoritmo
		for set_length in set_lengths:
			print('{0:10},{1:10f}'.format(set_length,tiempos_medios[algoritmo][set_length]))
			logging.debug(''.format(set_length,tiempos_medios[algoritmo][set_length]))
def run_insercion_peor_caso():
	return 0

def run_quicksort_peor_caso():
	return 0

def run_mergesort_peor_caso():
	return 0

def run_seleccion_peor_caso():
	return 0

def run_heapsort_peor_caso():
	return 0

def correr_tp():
	logging.debug('Construyendo sets de numeros aleatorios..')
	sets = []
	for i in enumerate(set_lengths):
		sets.append(gen_vector(10000))

	logging.debug('Calculando tiempos de ejecucion para cada set..')
	tiempos_ejecucion = calcular_tiempos_ejecucion(sets)

	logging.debug('Estimando tiempo medio de cada algoritmo..')
	tiempos_medios = calcular_tiempos_medios(tiempos_ejecucion)

	logging.debug('Resultados:')
	mostrar_resultados(tiempos_medios)

	logging.debug('Calculando tiempos de ejecucion en el peor caso..')
	run_insercion_peor_caso()
	run_quicksort_peor_caso()
	run_mergesort_peor_caso()
	run_seleccion_peor_caso()
	run_heapsort_peor_caso()

if __name__ == '__main__':
	correr_tp()
