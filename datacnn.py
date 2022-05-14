import numpy as np

def crear_data_entrada(series, n_ret=1, n_ava=1):
    '''
    Transformar datos para CNN.
    
    Parametros
    ----------
    series : np.array
        La serie de tiempo para ser transformada
    n_ret : int
        numero de observaciones hacia atrás
    n_ava : int
        numero de observaciones hacia adelante
        
    Devuelve
    -------
    X : np.array
        Arreglo precio
    y : np.array
        Arreglo de pronostico
    '''
    X = []
    y = []
    for precio in range(len(series) - n_ret - n_ava + 1):
        fin_precio = precio + n_ret
        avance_fin = fin_precio + n_ava
        X.append(series[precio:fin_precio])
        y.append(series[fin_precio:avance_fin])
    return np.array(X), np.array(y)

