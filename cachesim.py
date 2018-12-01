import sys
import math

#from cachesim import Access,CalculateTagIndexOffset,cacheTracker,cache


## Program Constants

# Input Values
cacheSize = 0		# Number of Bits
blockSize = 6		# Bytes 2^6 Cache Line Size
cacheWays = 0 		# 16 Way Set Associative Cache

# Calculated Values
numSets = 0
setBits = 0
tagBits = 0

cacheTracker = {'Cache Hits': 0, 'Cache Misses': 0,'Cache Accesses': 0}
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
	global numSets
	for x in range(numSets):
		setAssocCache.append({"queue":[]})

def AccessSAC(RW,addr):
	addr = int(addr,16)

	offset = addr & mask(blockSize)
	setNum = addr >> blockSize & mask(setBits)
	tag    = addr >> (setBits+blockSize) & mask(tagBits)

	# print("offset Mask: ",bin(offset))
	# print("SetNum Mask: ",bin(setNum))
	# print("Tag    Mask: ",bin(tag))

	#print(bin(addr))
	#print(bin(tag),bin(setNum),bin(offset))

	#return
	#print(setAssocCache)
	cacheTracker['Cache Accesses'] += 1
	if tag in setAssocCache[setNum]:
		#print("Cache Hit")
		cacheTracker['Cache Hits'] += 1
		SACacheHit(tag,setNum,offset)
	elif  tag not in setAssocCache[setNum]:
		#print("Cache Miss")
		cacheTracker['Cache Misses'] += 1
		SACacheMiss(tag,setNum,offset)

def SACacheHit(tag,setNum,offset):
	setAssocCache[setNum]["queue"].remove(tag)
	setAssocCache[setNum]["queue"].insert(0,tag)
	setAssocCache[setNum][tag] = offset

def SACacheMiss(tag,setNum,offset):
	if(len(setAssocCache[setNum]) < 17):
		setAssocCache[setNum][tag] = offset
		setAssocCache[setNum]["queue"].insert(0,tag)
	else:
		del setAssocCache[setNum][setAssocCache[setNum]["queue"].pop()]
		setAssocCache[setNum][tag] = offset
		setAssocCache[setNum]["queue"].insert(0,tag)

def CalculateValues():
	global numSets,setBits,tagBits
	numSets = int((2**cacheSize)/(2**blockSize * 2**cacheWays))
	setBits = int(math.log(numSets,2))
	tagBits = cacheSize - blockSize - setBits
	print("NumSets:",numSets,"\nSetBits:",setBits,"\nTagBits:",tagBits)

def mask(amount):
	return 2**amount -1




#
#
## Program Start
#
#

if len(sys.argv) < 5:
	print("Usage: python3 CacheSim.py <File Name> <Cache Size: 2^N> <Block Size: 2^N> <Cache Ways: 2^N>")
	print("\t-f USE FIFO instead of LRU")
	sys.exit(1)
file = open(sys.argv[1],"r")
cacheSize = int(sys.argv[2])
blockSize = int(sys.argv[3])
cacheWays = int(sys.argv[4])
print("cacheSize: ",cacheSize,"\nblockSize: ",blockSize,"\ncacheWays: ",cacheWays,sep="")

CalculateValues()
SetUpSetAssocCache()
# Call your code in this loop
while True:
	dataTuple = ReadFileLine()
	if(dataTuple == None):
		break
	elif(dataTuple == -1):
		continue
	else:
		try:
			AccessSAC(dataTuple[1],dataTuple[2])
		except Exception as e:
			continue


print(cacheTracker)
print("Cache Miss Rate: {0:.2f}%".format((100/cacheTracker['Cache Accesses']) * cacheTracker['Cache Misses']),sep="")
file.close()