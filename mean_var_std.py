import numpy as np
def calculate(data):
  if len(data)!=9:
    raise ValueError("List must contain nine numbers.")
  matrix1=np.reshape(data,(3,3))
  stats={'mean':[np.mean(matrix1,axis=0).tolist(),np.mean(matrix1,axis=1).tolist(),np.mean(matrix1).tolist()],'variance':[np.var(matrix1,axis=0).tolist(),np.var(matrix1,axis=1).tolist(),np.var(matrix1).tolist()],'standarddeviation':[np.std(matrix1,axis=0).tolist(),np.std(matrix1,axis=1).tolist(),np.std(matrix1).tolist()],'max':[np.max(matrix1,axis=0).tolist(),np.max(matrix1,axis=1).tolist(),np.max(matrix1).tolist()],'min':[np.min(matrix1,axis=0).tolist(),np.min(matrix1,axis=1).tolist(),np.min(matrix1).tolist()],'sum':[np.sum(matrix1,axis=0).tolist(),np.sum(matrix1,axis=1).tolist(),np.sum(matrix1).tolist()]}
  return stats
