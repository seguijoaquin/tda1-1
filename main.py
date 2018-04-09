import numpy

from graficador import *
from quicksort import quicksort
from merge import merge_sort
from insercion import insercion
from seleccion import seleccion
from heapsort import heapsort

algoritmos = {
	'Quicksort' : quicksort,
	'Mergesort' : merge_sort,
	'Insercion' : insercion,
	'Seleccion' : seleccion,
	'Heapsort' : heapsort
}

rangos = [50,100,500,1000,2000,3000,4000,5000,7500,10000]

def construir_sets():
	sets = []
	for i in enumerate(rangos):
		sets.append(gen_vector(10000))
	return sets


def ordenar(sets,algoritmo):
	results = {}
	for r in rangos:
		results[r] = []
	for r in rangos:
		log('Ordenando set de {} elementos.'.format(r))
		for set in sets:
			results[r].append(performance(set[:r],algoritmo))
	return results

def calcular_tiempos_ejecucion(sets):
	results = {}
	for clave in algoritmos:
		log('Calculando tiempos ejecucion de {}.'.format(clave))
		results[clave] = ordenar(sets,algoritmos[clave])
	return results

def calcular_tiempos_medios(tiempos_ejecucion):
	tiempos_medios = {}
	for key,value in enumerate(tiempos_ejecucion):
		tiempos_medios[value] = {}
		for key_set,r_value in enumerate(rangos):
			tiempos_medios[value][r_value] = numpy.mean(tiempos_ejecucion[value][r_value])
			log('Tiempo medio de {} para {} elementos: {}'.format(value,r_value,tiempos_medios[value][r_value]))
	
	return tiempos_medios

def mostrar_resultados(tiempos_medios):
	for algoritmo in tiempos_medios:
		log('Algoritmo: {}'.format(algoritmo))
		for r in rangos:
			log('{0:10},{1:10f}'.format(r,tiempos_medios[algoritmo][r]))

def graficar(tiempos_medios):
	for i in tiempos_medios:
		fig, ax = plt.subplots(1,1, figsize=(8, 6))
		ax.plot(*zip(*sorted(tiempos_medios[i].items())))
		fig.suptitle(i, fontsize=16)
		plt.xlabel('Elementos [un]', fontsize=12)
		plt.ylabel('Tiempo [seg]', fontsize=12)
		fig.savefig(i + '.png')

def generar_set_desc():
	return range(10000,0,-1)

def peores_casos():
	set_desc = generar_set_desc()
	

def correr_tp():
	log('Construyendo sets de numeros aleatorios..')
	sets = construir_sets()

	log('Calculando tiempos de ejecucion para cada set..')
	tiempos_ejecucion = calcular_tiempos_ejecucion(sets)

	log('Estimando tiempo medio de cada algoritmo..')
	tiempos_medios = calcular_tiempos_medios(tiempos_ejecucion)

	log('Resultados:')
	mostrar_resultados(tiempos_medios)

	log('Graficando Resultados:')
	graficar(tiempos_medios)

#	log('Construyendo peores casos..')
#	peores_casos()
	
#	log('Ejecutando Gale-Shapley')

if __name__ == '__main__':
	correr_tp()
