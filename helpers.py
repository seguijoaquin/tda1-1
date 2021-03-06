# coding: utf-8
import time
import random
import sys
from matplotlib import pyplot as plt

import logging
FORMAT = "%(asctime)-15s - %(message)s"
logging.basicConfig(format=FORMAT,filename='tp.log',level=logging.DEBUG)

def log(val):
    logging.debug(val)
    dump(val)

def performance(vector, algoritmo):
    inicio = time.time()
    algoritmo(vector)
    return time.time()-inicio

def gen_vector(length):
    i = 0
    vector = []
    while i < length:
        vector.append(random.randrange(1000))
        i+=1
    return vector

def graficar(tiempos_medios,peorCaso=False):
	file_suffix = '_peor_caso' if peorCaso else ''
	title_suffix = ' Peor Caso' if peorCaso else ''
	for i in tiempos_medios:
		fig, ax = plt.subplots(1,1, figsize=(8, 6))
		ax.plot(*zip(*sorted(tiempos_medios[i].items())))
		fig.suptitle(i + title_suffix, fontsize=16)
		plt.xlabel('Elementos [un]', fontsize=12)
		plt.ylabel('Tiempo [seg]', fontsize=12)
		fig.savefig(i + file_suffix + '.png')

def graficarAmbos(tiempos_medios,tiempos_medios_pc):
    for i in tiempos_medios:
        fig, ax = plt.subplots(1,1, figsize=(8, 6))
        line1, = ax.plot(*zip(*sorted(tiempos_medios[i].items())),label="Caso Promedio", linewidth=4)
        line2, = ax.plot(*zip(*sorted(tiempos_medios_pc[i].items())),label="Peor Caso", linestyle='--')
        first_legend = plt.legend(handles=[line1], loc=4)
        ax.add_artist(first_legend)
        ax.legend(handles=[line2], loc=1)
        fig.suptitle(i + ' Promedio y Peor Caso', fontsize=16)
        plt.xlabel('Elementos [un]', fontsize=12)
        plt.ylabel('Tiempo [seg]', fontsize=12)
        fig.savefig(i + '_ambos.png')
        
def graficarTeoricos(tiempos_medios,tiempos_medios_teoricos):
    for i in tiempos_medios:
        fig, ax = plt.subplots(1,1, figsize=(8, 6))
        line1, = ax.plot(*zip(*sorted(tiempos_medios[i].items())),label="Caso Promedio", linewidth=4)
        line2, = ax.plot(*zip(*sorted(tiempos_medios_teoricos[i].items())),label="Caso Teorico", linestyle='--')
        first_legend = plt.legend(handles=[line1], loc=4)
        ax.add_artist(first_legend)
        ax.legend(handles=[line2], loc=1)
        fig.suptitle(i + ' Promedio y Teorico', fontsize=16)
        plt.xlabel('Elementos [un]', fontsize=12)
        plt.ylabel('Tiempo [seg]', fontsize=12)
        fig.savefig(i + '_ambos_teoricos.png')

def dump(obj, nested_level=0, output=sys.stdout):
    spacing = '   '
    if type(obj) == dict:
        print('%s{' % ((nested_level) * spacing), file=output)
        for k, v in obj.items():
            if hasattr(v, '__iter__'):
                print('%s%s:' % ((nested_level + 1) * spacing, k),file=output)
                dump(v, nested_level + 1, output)
            else:
                print('%s%s: %s' % ((nested_level + 1) * spacing, k, v),file=output)
        print('%s}' % (nested_level * spacing),file=output)
    elif type(obj) == list:
        print('%s[' % ((nested_level) * spacing),file=output)
        for v in obj:
            if hasattr(v, '__iter__'):
                dump(v, nested_level + 1, output)
            else:
                print('%s%s' % ((nested_level + 1) * spacing, v),file=output)
        print('%s]' % ((nested_level) * spacing),file=output)
    else:
        print('%s%s' % (nested_level * spacing, obj),file=output)