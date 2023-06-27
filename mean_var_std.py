import numpy as np

def calculate(list):
  if len(list) != 9:
      raise ValueError("List must contain nine numbers.")

  arr = np.array([list]).reshape(3,3)

  meanrow = np.mean(arr, axis=0).tolist()
  meancol = np.mean(arr, axis=1).tolist()
  meanflat = np.mean(arr).tolist()
  
  varrow = np.var(arr, axis=0).tolist()
  varcol = np.var(arr, axis=1).tolist()
  varflat = np.var(arr).tolist()

  stdrow = np.std(arr, axis=0).tolist()
  stdcol = np.std(arr, axis=1).tolist()
  stdflat = np.std(arr).tolist()

  maxrow = np.max(arr, axis=0).tolist()
  maxcol = np.max(arr, axis=1).tolist()
  maxflat = np.max(arr).tolist()

  minrow = np.min(arr, axis=0).tolist()
  mincol = np.min(arr, axis=1).tolist()
  minflat = np.min(arr).tolist()

  sumrow = np.sum(arr, axis=0).tolist()
  sumcol = np.sum(arr, axis=1).tolist()
  sumflat = np.sum(arr).tolist()
  
  return {
    'mean': [meanrow, meancol, meanflat],
    'variance': [varrow, varcol, varflat],
    'standard deviation': [stdrow, stdcol, stdflat],
    'max': [maxrow, maxcol, maxflat],
    'min': [minrow, mincol, minflat],
    'sum': [sumrow, sumcol, sumflat]
  }   