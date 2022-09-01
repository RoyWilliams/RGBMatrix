from datetime import datetime
import numpy as np
import settings

def now():
    return datetime.utcnow().strftime("%m/%d %H:%M:%S")

def iterate(Z):
    # find number of neighbors that each square has
    N = np.zeros(Z.shape)
    N[1:, 1:] += Z[:-1, :-1]
    N[1:, :-1] += Z[:-1, 1:]
    N[:-1, 1:] += Z[1:, :-1]
    N[:-1, :-1] += Z[1:, 1:]
    N[:-1, :] += Z[1:, :]
    N[1:, :] += Z[:-1, :]
    N[:, :-1] += Z[:, 1:]
    N[:, 1:] += Z[:, :-1]
    # a live cell is killed if it has fewer than 2 or more than 3 neighbours.
    part1 = ((Z == 1) & (N < 4) & (N > 1))
    # a new cell forms if a square has exactly three members
    part2 = ((Z == 0) & (N == 3))
    return (part1 | part2).astype(int)

class state():
    def __init__(self, n):
        self.n = n
        self.old_lasair_hits = [0]*n*n
        self.ca = np.zeros((n,n), dtype=np.int8)
        self.lasair_display = np.zeros((n, n, 3))
        self.ca_display = np.zeros((n, n, 3))
        self.Qmax = 0

    def display(self, lasair_hits):
        for i in range(self.n):
            for j in range(self.n):
                k = i + j*self.n
                Q = lasair_hits[k] - self.old_lasair_hits[k]
                if Q > 0:
                    self.ca[j,i] = 1
                    r = self.lasair_display[j,i,0]
                    g = self.lasair_display[j,i,1]
                    b = self.lasair_display[j,i,2]
                    if   Q < self.Qmax/6: r = (1+r)/2
                    elif Q < self.Qmax/3: g = (1+g)/2
                    else:                 r = g = b = 1
                    self.lasair_display[j,i,0] = r
                    self.lasair_display[j,i,1] = g
                    self.lasair_display[j,i,2] = b
                    self.old_lasair_hits[k] = lasair_hits[k]
                    if Q > self.Qmax: 
                        self.Qmax = Q
                        print(now(), 'Qmax', self.Qmax)

        for i in range(3):
            self.lasair_display[:,:,i] -= self.lasair_display[:,:,i]/settings.lasair_fade[i]

        self.ca = iterate(self.ca)
        for i in range(3):
            self.ca_display[:,:,i] = self.ca_display[:,:,i] + \
                (self.ca[:,:]-self.ca_display[:,:,i])*settings.life_fade[i]

        return np.maximum(self.lasair_display, self.ca_display)
