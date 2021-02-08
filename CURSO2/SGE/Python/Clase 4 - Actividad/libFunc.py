def divisores(n):
    
    m = 1
    div = []
    
    while (m <= n/2):
        if (n%m == 0):
            div.append(m)
        m += 1
    
    div.append(n)
    
    return div


def conteo(n):
    
    div = divisores(n)
    num = len(div)
    
    return num


def primo(n):
    
    if (conteo(n) == 2):
        return True
    else:
        return False
    

def perfecto(n):
    
    div = divisores(n)
    suma = sum(div) - n
    
    if (suma == n):
        return True
    else:
        return False
    
    
def cifras(n):
    
    m = n
    cif = []
    
    while (m >= 1):
        m = int(m/10)
        m = m * 10
        cif.append(int(n-m))
        m = m/10
        n = m
        
    cif.reverse()
        
    return cif


def sumad(n):
    
    cif = cifras(n)   
    suma = sum(cif)
    
    return suma