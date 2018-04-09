# coding: utf-8
import time
import random
from matplotlib import pyplot as plt

import logging
FORMAT = "%(asctime)-15s - %(message)s"
logging.basicConfig(format=FORMAT,filename='main.log',level=logging.INFO)

def log(val):
	print(val)
	logging.debug(val)


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

    
    
