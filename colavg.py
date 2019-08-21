def colavg():
  import pandas as pd
  import numpy as np
  df = pd.read_csv(input('Enter filename here: '), sep=';', decimal = ',', index_col = 0)
  columns_total = df.shape[1] #Get number of columns
  num_columns = int(input('Enter amount of columns to take average off: ')) #number of columns to take the average off
  steps = columns_total / num_columns #number of columns in output df
  
  df2 = pd.DataFrame() #Create empty dataframe
  series = np.linspace(0, columns_total-num_columns, steps, dtype = int)
  series2 = series + num_columns #Make 2 series with steps in between to fill i&j in the loop
  
  for i,j in zip(series,series2): #for the difference between i and j:
    col = df.iloc[:, i:j] # col holds all rows and column i:j-1
    df2[f'{i}-{j-1}'] = col.mean(axis = 1) #take the mean of col and add it to a new column in df2
  df2.to_csv(str(input("Enter filename here, file will be in the same path as the script: ")), sep=';', decimal=',')
