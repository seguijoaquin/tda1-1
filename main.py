import numpy

from graficador import *
from quicksort import quicksort
from merge import merge_sort
from insercion import insercion
from seleccion import seleccion

algoritmos = {
	'Quicksort' : quicksort,
	'Mergesort' : merge_sort
#	'Insercion' : insercion,
#	'Seleccion' : seleccion
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

def graficar(largo=200):
	for algo in algoritmos:
		fig, ax = plt.subplots(1, 1, figsize=(8, 5))
		vectores = [gen_vector(i*3) for i in range(largo)]
		largos = [len(v) for v in vectores]
		performs = [performance(v, algoritmos[algo]) for v in vectores]
		ax.plot(largos, performs)
		fig.suptitle(algo, fontsize=20)
		plt.xlabel('Elementos', fontsize=18)
		plt.ylabel('Tiempo', fontsize=16)
		fig.savefig(algo + '.png')



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

def run_peores_casos():
        run_insercion_peor_caso()
        run_quicksort_peor_caso()
        run_mergesort_peor_caso()
        run_seleccion_peor_caso()
        run_heapsort_peor_caso()

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
#	graficar(tiempos_medios)
	graficar()

	log('Calculando tiempos de ejecucion en el peor caso..')
	run_peores_casos()

if __name__ == '__main__':
	correr_tp()
