import numpy
import sys

from helpers import log, performance, gen_vector, graficar, graficarAmbos, graficarTeoricos
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

rangos = [50, 100, 500, 1000, 2000, 3000, 4000, 5000, 7500, 10000]

tiempos_medios_teoricos = { 
	'Seleccion' : { 50: 0.00009,
					100: 0.0003,
					500: 0.009,
					1000: 0.0362,
					2000: 0.1447,
					3000: 0.3254,
					4000: 0.5785,
					5000: 0.9038,
					7500: 2.0333,
					10000: 3.6145
	}, 
	'Insercion' : { 50: 0.0001,
					100: 0.0005,
					500: 0.0126,
					1000: 0.05,
					2000: 0.1995,
					3000: 0.4485,
					4000: 0.7971,
					5000: 1.2451,
					7500: 2.8005,
					10000: 4.9779 
	}, 
	'Quicksort' : { 50: 0.000069,
					100: 0.00016,
					500: 0.0011,
					1000: 0.00245,
					2000: 0.00539,
					3000: 0.00851,
					4000: 0.01176,
					5000: 0.0151,
					7500: 0.0237,
					10000: 0.03266
	}, 
	'Mergesort' : { 50: 0.0002,
					100: 0.0004,
					500: 0.0027,
					1000: 0.006,
					2000: 0.0131,
					3000: 0.0222,
					4000: 0.0286,
					5000: 0.041,
					7500: 0.0585,
					10000: 0.0878
	}, 
	'Heapsort'  : { 50: 0.0003,
					100: 0.0008,
					500: 0.0058,
					1000: 0.013,
					2000: 0.0289,
					3000: 0.0459,
					4000: 0.0637,
					5000: 0.082,
					7500: 0.129,
					10000: 0.179 
	}
	}


def construir_sets():
	sets = []
	for _ in enumerate(rangos):
		sets.append(gen_vector(10000))
	return sets


def construir_sets_peor_caso():
	set_base = []
	[(set_base.append(i)) for i in range(10000, 0, -1)]
	sets = [set_base.copy() for _ in range(10)]
	return sets


def ordenar(sets, algoritmo):
	results = {}
	for r in rangos:
		results[r] = []
	for r in rangos:
		log('--- Ordenando set de {} elementos.'.format(r))
		for set in sets:
			results[r].append(performance(set[:r], algoritmo))
	return results


def calcular_tiempos_ejecucion(sets):
	results = {}
	for clave in algoritmos:
		log('-- Calculando tiempos ejecucion de {}.'.format(clave))
		results[clave] = ordenar(sets, algoritmos[clave])
	return results


def calcular_tiempos_medios(tiempos_ejecucion):
	tiempos_medios = {}
	for _, value in enumerate(tiempos_ejecucion):
		tiempos_medios[value] = {}
		for _, r_value in enumerate(rangos):
			tiempos_medios[value][r_value] = numpy.mean(tiempos_ejecucion[value][r_value])
			log('-- Tiempo medio de {} para {} elementos [s]: {}'.format(value, r_value, tiempos_medios[value][r_value]))
	
	return tiempos_medios


def mostrar_resultados(tiempos_medios):
	for algoritmo in tiempos_medios:
		log('-- Algoritmo: {}'.format(algoritmo))
		for r in rangos:
			log('{0:10}: {1:10f} s'.format(r, tiempos_medios[algoritmo][r]))


def correr_tp():

	sys.setrecursionlimit(1000000)  # Avoiding Recursive Quicksort overflow

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
	graficar(tiempos_medios_pc, True)

	graficarAmbos(tiempos_medios, tiempos_medios_pc)
	
	graficarTeoricos(tiempos_medios, tiempos_medios_teoricos)


if __name__ == '__main__':
	correr_tp()
