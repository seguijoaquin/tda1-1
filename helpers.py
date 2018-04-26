# coding: utf-8
import time
import random
import sys
from matplotlib import pyplot as plt

#import logging
#FORMAT = "%(asctime)-15s - %(message)s"
#logging.basicConfig(format=FORMAT,filename='main.log',level=logging.DEBUG)

def log(val):
    dump(val)
    #print(val)
	#logging.debug(val)

def performance(vector, algoritmo):
    inicio = time.time()
    algoritmo(vector)
    return time.time()-inicio

def gen_vector(length):
    return [random.randrange(1000) for _ in range(length)]
    
def graficar_algoritmo(algoritmo, largo=200):
    fig, ax = plt.subplots(1, 1, figsize=(5, 5))
    vectores = [gen_vector(i*3) for i in range(largo)]
    largos = [len(v) for v in vectores]
    performs = [performance(v, algoritmo) for v in vectores]
    ax.plot(largos, performs)
    return ax

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

def dump(obj, nested_level=0, output=sys.stdout):
    spacing = '   '
    if type(obj) == dict:
        print >> output, '%s{' % ((nested_level) * spacing)
        for k, v in obj.items():
            if hasattr(v, '__iter__'):
                print >> output, '%s%s:' % ((nested_level + 1) * spacing, k)
                dump(v, nested_level + 1, output)
            else:
                print >> output, '%s%s: %s' % ((nested_level + 1) * spacing, k, v)
        print >> output, '%s}' % (nested_level * spacing)
    elif type(obj) == list:
        print >> output, '%s[' % ((nested_level) * spacing)
        for v in obj:
            if hasattr(v, '__iter__'):
                dump(v, nested_level + 1, output)
            else:
                print >> output, '%s%s' % ((nested_level + 1) * spacing, v)
        print >> output, '%s]' % ((nested_level) * spacing)
    else:
        print >> output, '%s%s' % (nested_level * spacing, obj)