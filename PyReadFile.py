#! /usr/bin/python

import sys

if len(sys.argv) < 2:
	print("filename needed as command argument")
	sys.exit(1)
file = open(sys.argv[1],"r")



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



# Call your code in this loop
while True:
	dataTuple = ReadFileLine()
	if(dataTuple == None):
		break
	elif(dataTuple == -1):
		continue
	else:
		Access(dataTuple[1],dataTuple[2])

def Access(RW,addr):
	print(RW,addr)


file.close()