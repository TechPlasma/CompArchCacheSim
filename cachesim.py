import sys
import numpy as np
import pandas as pd

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

columns = ['Tag','Validbit', 'data', 'timestamp']
df= pd.DataFrame(columns=columns)
print(df.columns)


#def Access(RW,addr):


    