from libFunc import *
import random

n = random.randint(1, 99)
m = random.randint(1, 99)

while not(primo(n) and primo(m) and primo(n+m)):
    n = random.randint(1, 99)
    m = random.randint(1, 99)

print(n, "es primo", m, "es primo y su suma (", (n+m),") también lo es" )