from functools import lru_cache

cache = {}

def fibonacci_cached(n: int) -> int:
    if n in cache:
        return cache[n]
    
    if n == 0 or n == 1:
        return n
    
    result = fibonacci_cached(n-2) + fibonacci_cached(n-1)
    cache[n] = result
    return cache[n]


#Esta funcao de baixo funciona exatamente como a de cima, mas com recursos mais avancados
#Grava as entradas e saidas....
@lru_cache(maxsize=256)
def fibonacci_lru_cached(n: int) -> int:
    if n == 0 or n == 1:
        return n
    
    return fibonacci_lru_cached(n-2) + fibonacci_lru_cached(n-1)