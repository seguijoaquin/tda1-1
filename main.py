import numpy

import logging

FORMAT = "%(asctime)-15s    %(sort)-8s     %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)

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

def calcular_tiempos_ejecucion(sets):
	results = {}
	results_total = {}
	for set_lenght in set_lengths:
		results[set_lenght] = []
	for clave in algoritmos:
		algoritmo = algoritmos[clave]
		for set_length in set_lengths:
			for set in sets:
				logging.debug('Calculando tiempo ejecucion de {} con {} elementos.'.format(clave,set_length))
				vector = set[:set_length]
				tiempo = performance(vector,algoritmo)
				results[set_lenght].append(tiempo)
		results_total[clave] = results[set_length]
	return results_total

def calcular_tiempos_medios(tiempos_ejecucion):
	tiempos_medios = {}
	for algoritmo in tiempos_ejecucion:
		tiempos_medios[algoritmo] = {}
		for set_length in set_lengths:
			logging.debug('Accediendo a tiempos_ejecucion en {} , {} ',format(algoritmo,set_length))
			tiempos_medios[algoritmo][set_length] = numpy.mean(tiempos_ejecucion[algoritmo][set_length])
	
	return tiempos_medios

def mostrar_resultados(tiempos_medios):
	for algoritmo in tiempos_medios:
		print algoritmo
		for set_length in set_lengths:
			print('{0:10},{1:10f}'.format(set_length,tiempos_medios[algoritmo][set_length]))

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
	for i in range(0, 10):
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
