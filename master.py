import settings
import time
import random
import multiprocessing
import numpy as np
import lasair

# The first is a matplotlib screen, the second for the real matriz
#from screen import init, show
from led_matrix import init, show

# The first is for mock kafka, the second for the real thing
#import mockkafka as kafka
import kafka

n = 32
L = lasair.state(n)

def run_display(pass_shmarray):
    global L
    shmarray = pass_shmarray
    matrix = init()
    while 1:
        a = L.display(shmarray)
        show(a, matrix)
        time.sleep(settings.lasair_delay)

if __name__ == '__main__':
    array = multiprocessing.Array("i", n*n)
    process1 = multiprocessing.Process(target=kafka.get_kafka, args=[array])
    process2 = multiprocessing.Process(target=run_display,     args=[array])

    process1.start()
    process2.start()

    process1.join()
    process2.join()
