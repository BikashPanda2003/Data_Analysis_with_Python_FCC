import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    A=np.array([list[0:3],
                list[3:6],
                list[6:9]])
    calculations={}

    calculations['mean']=[np.mean(A,axis=0).tolist(),np.mean(A,axis=1).tolist(),np.mean(A)]
    calculations['variance']=[np.var(A,axis=0).tolist(),np.var(A,axis=1).tolist(),np.var(A)]
    calculations['standard deviation']=[np.std(A,axis=0).tolist(),np.std(A,axis=1).tolist(),np.std(A)]
    calculations['max']=[np.max(A,axis=0).tolist(),np.max(A,axis=1).tolist(),np.max(A)]
    calculations['min']=[np.min(A,axis=0).tolist(),np.min(A,axis=1).tolist(),np.min(A)]
    calculations['sum']=[np.sum(A,axis=0).tolist(),np.sum(A,axis=1).tolist(),np.sum(A)]
    return calculations



  
  


