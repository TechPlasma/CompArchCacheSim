import sys
tagStart = 0
indexStart = 7
offsetStart = 12

cacheTracker = {'Cache Hits': 0, 'Cache Misses': 0,'Cache Accesses': 0}
cache = {}
cacheQue = []

def Access(RW,addr):
	tag = addr[indexStart:]
	loc = addr
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


## Todo
#	- Implement Set Associative Cache
#	- 


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