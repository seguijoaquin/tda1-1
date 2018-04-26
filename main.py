import numpy

from helpers import log, performance, gen_vector, graficar
from quicksort import quicksort
from merge import merge_sort
from insercion import insercion
from seleccion import seleccion
from heapsort import heapsort

algoritmos = {
#	'Quicksort' : quicksort,
#	'Mergesort' : merge_sort,
	'Insercion' : insercion,
	'Seleccion' : seleccion,
#	'Heapsort' : heapsort
}

rangos = [50,100,500,1000,2000,3000,4000,5000,7500,10000]

def construir_sets():
	sets = []
	for i in enumerate(rangos):
		sets.append(gen_vector(10000))
	return sets

def construir_sets_peor_caso():
	sets = [range(10000,0,-1) for _ in range(10)]
	return sets

def ordenar(sets,algoritmo):
	results = {}
	for r in rangos:
		results[r] = []
	for r in rangos:
		log('--- Ordenando set de {} elementos.'.format(r))
		for set in sets:
			results[r].append(performance(set[:r],algoritmo))
	return results

def calcular_tiempos_ejecucion(sets):
	results = {}
	for clave in algoritmos:
		log('-- Calculando tiempos ejecucion de {}.'.format(clave))
		results[clave] = ordenar(sets,algoritmos[clave])
	return results

def calcular_tiempos_medios(tiempos_ejecucion):
	tiempos_medios = {}
	for key,value in enumerate(tiempos_ejecucion):
		tiempos_medios[value] = {}
		for key_set,r_value in enumerate(rangos):
			tiempos_medios[value][r_value] = numpy.mean(tiempos_ejecucion[value][r_value])
			log('-- Tiempo medio de {} para {} elementos [s]: {}'.format(value,r_value,tiempos_medios[value][r_value]))
	
	return tiempos_medios

def mostrar_resultados(tiempos_medios):
	for algoritmo in tiempos_medios:
		log('-- Algoritmo: {}'.format(algoritmo))
		for r in rangos:
			log('{0:10}: {1:10f} s'.format(r,tiempos_medios[algoritmo][r]))

def correr_tp():
	log('- Construyendo 10 sets de numeros aleatorios de 1 a 1000..')
	sets = construir_sets()

	log('- Calculando tiempos de ejecucion para cada set..')
	tiempos_ejecucion = calcular_tiempos_ejecucion(sets)

	log('- Estimando tiempo medio de cada algoritmo..')
	tiempos_medios = calcular_tiempos_medios(tiempos_ejecucion)

	log('- Resultados:')
	mostrar_resultados(tiempos_medios)

	log('- Graficando Resultados: OK')
	graficar(tiempos_medios)

	log('- Construyendo peores casos..')
	sets_pc = construir_sets_peor_caso()

	log('- Calculando tiempos de ejecucion para cada set en peor caso..')
	tiempos_ejecucion_pc = calcular_tiempos_ejecucion(sets_pc)

	log('- Estimando tiempo medio de cada algoritmo en peor caso..')
	tiempos_medios_pc = calcular_tiempos_medios(tiempos_ejecucion_pc)

	log('- Resultados peor caso:')
	mostrar_resultados(tiempos_medios_pc)

	log('- Graficando Resultados peor caso: OK')
	graficar(tiempos_medios_pc,True)

if __name__ == '__main__':
	correr_tp()
