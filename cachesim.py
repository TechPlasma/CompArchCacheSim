import sys

#from cachesim import Access,CalculateTagIndexOffset,cacheTracker,cache


## Program Constants

cacheSize = 48		# Number of Bits
cacheLineSize = 6	# Bytes 2^6
cacheWay = 4 		# 16 Way Set Associative Cache
numSets = 7

## Data for Cache Calculator
scale = 16 ## equals to hexadecimal
#num_of_bits = cacheSize

tagStart 	= 0
indexStart 	= 0 #7
offsetStart = 42 #42

cacheTracker = {'Cache Hits': 0, 'Cache Misses': 0,'Cache Accesses': 0}
cache = {}
cacheQue = []
setAssocCache = []



# Reads the Next Line of input
# Returns:
# 	- None : End of File
# 	- -1 : ERROR Reading Data
# 	- Tuple : ("PC Address","R/W","Memory Address")
def ReadFileLine():
	try:
		inputLine = file.readline()
		if inputLine == "":
			return None

		inputLine = inputLine.rstrip('\n')
		lineData = inputLine.split(" ")
		dataTuple = (lineData[0].replace(":",""),lineData[1],lineData[2])
		return dataTuple
	except Exception as e:
		return -1 #print(e)


def SetUpSetAssocCache():
	numSets = int((cacheSize - cacheLineSize)/cacheLineSize)
	for x in range(numSets):
		setAssocCache.append({})




def CalculateTagIndexOffset():
	offsetStart = cacheSize - cacheLineSize
	indexStart = cacheSize - cacheLineSize - cacheWay
	print("TagStart:\t",tagStart,"\nIndexStart:\t",indexStart,"\nOffsetStart:\t",offsetStart)

#print("TagStart:\t",tagStart,"\nIndexStart:\t",indexStart,"\nOffsetStart:\t",offsetStart)
def AccessFA(RW,addr):

	if(addr[0:2] == "Ox"):
		addr = addr[2:]
	addr = str(bin(int(addr, scale))[2:].zfill(cacheSize))

	tag = addr[tagStart:offsetStart]
	loc = addr[offsetStart:]


	cacheTracker['Cache Accesses'] += 1
	if tag in cache:
		#print("Cache Hit")
		cacheTracker['Cache Hits'] += 1
		CacheHit(loc,tag)
	elif  tag not in cache:
		#print("Cache Miss")
		cacheTracker['Cache Misses'] += 1
		CacheMiss(loc,tag)
	#print(tag)
	#print(cache)
	#print(cacheQue)

def AccessSAC(RW,addr):
	if(addr[0:2] == "Ox"):
		addr = addr[2:]
	addr = str(bin(int(addr, scale))[2:].zfill(cacheSize))

	tag = addr[tagStart:offsetStart]
	index = addr[indexStart:offsetStart]
	loc = addr[offsetStart:]


	cacheTracker['Cache Accesses'] += 1
	if tag in setAssocCache[getSet(tag)]:
		#print("Cache Hit")
		cacheTracker['Cache Hits'] += 1
		SACacheHit(loc,tag)
	elif  tag not in setAssocCache[getSet(tag)]:
		#print("Cache Miss")
		cacheTracker['Cache Misses'] += 1
		SACacheMiss(loc,tag)
	#print(tag)
	#print(cache)
	#print(cacheQue)

def CacheHit(loc,tag):
	cacheQue.remove(tag)
	cacheQue.insert(0,tag)
	cache[tag] = loc

def CacheMiss(loc,tag):
	if(len(cache) < 32):
		cache[tag] = loc
		cacheQue.insert(0,tag)
	else:
		del cache[cacheQue.pop()]
		cache[tag] = loc
		cacheQue.insert(0,tag)

def SACacheHit(loc,tag):
	cacheQue.remove(tag)
	cacheQue.insert(0,tag)
	setAssocCache[getSet(tag)][tag] = loc

def SACacheMiss(loc,tag):
	if(len(setAssocCache[getSet(tag)]) < 16):
		setAssocCache[getSet(tag)][tag] = loc
		cacheQue.insert(0,tag)
	else:
		del setAssocCache[getSet(tag)][cacheQue.pop()]
		setAssocCache[getSet(tag)][tag] = loc
		cacheQue.insert(0,tag)

def getSet(tag):
	print(int(tag,2))
	return int(tag,2)%numSets


## Program Start




if len(sys.argv) < 2:
	print("filename needed as command argument")
	sys.exit(1)
file = open(sys.argv[1],"r")



CalculateTagIndexOffset()
SetUpSetAssocCache()
# Call your code in this loop
while True:
	dataTuple = ReadFileLine()
	if(dataTuple == None):
		break
	elif(dataTuple == -1):
		continue
	else:
		AccessFA(dataTuple[1],dataTuple[2])



print(cache)
print(len(cache))
print(cacheTracker)
print("Cache Miss Rate: {0:.2f}%".format((100/cacheTracker['Cache Accesses']) * cacheTracker['Cache Misses']),sep="")
file.close()