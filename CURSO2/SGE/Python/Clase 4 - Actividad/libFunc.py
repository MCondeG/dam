def conteo(n):
    
    m = 1
    cont = 1
    
    while (m <= n/2):
        if (n%m == 0):
            cont += 1
        m += 1
        
    return (cont)

def primo(n):
    if (conteo(n) == 2):
        return True
    else:
        return False