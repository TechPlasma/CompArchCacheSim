import sys


print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))

CacheDict = {'Tag': 0, 'Valid': 0, 'Data': 0}

def Access(RW,addr):
    CacheDict = {'Tag': 0, 'Valid': 0, 'Data': 0}
    L=[]
    if addr in CacheDict.keys():
        L[0] = addr
    elif  addr not in CacheDict.keys():
         L.pop()



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