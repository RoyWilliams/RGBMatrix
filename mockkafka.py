import time
import random

n = 32
def init():
    return

def get_kafka(array):
    while 1:
        i = random.randrange(n)
        j = random.randrange(n)
        k = i*n+j
        array[k] += 1
        if random.random() < 0.1:
            time.sleep(10)
        else:
            time.sleep(0.01)

if __name__ == "__main__":
    init()
    get_kafka([0]*n*n)
