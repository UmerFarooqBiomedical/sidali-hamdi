import pandas as pd
def callfunction_detection():
  x = pd.read_csv("xgSocket.data")
  y = pd.read_csv("cellsStatus.data")
  if "NOK" in str(x):
    error = "E1: No communication with camera controller."
    ecolor = "Red"
    state = "xgSocket.data : NOK\n"
    bg_color2 = "red"
  elif "OK" in str(x):
    if "NOK" in str(y):
      error = "E7: Error detected with detection cells."
      ecolor = "Red"
      state = "xgSocket.data : OK\n cellsStatus.data : NOK\n"
      bg_color2 = "Orange"
    elif "OK" in str(y):
      error = "No issues. System working fine."
      ecolor = "Green"
      state = "xgSocket.data : OK\n cellsStatus.data : OK\n"
      bg_color2 = "Green"
  return bg_color2, state, error, ecolor
