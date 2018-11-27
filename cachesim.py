import sys
import numpy as np
import pandas as pd

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

columns = ['Tag','Validbit', 'data', 'timestamp']

cachedf= pd.DataFrame(columns=columns)
print(df.columns)

def Access(RW,addr):
#Check if in cache
#cut out the bits( determine setID)
#search set determine if addr is in cache, tag comparison
#check valid bit

#if hit
# -update timestamp of cache line that was hit

# if miss
#  -find slot
#  -update slot
#    -set valid bit to 1
#    -update tag
#    -update timestamp