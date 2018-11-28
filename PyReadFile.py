#! /usr/bin/python

import sys
print("#args=", len(sys.argv))
if len(sys.argv) < 2:
	print("filename needed as command argument")
	sys.exit(1)
file = open(sys.argv[1],"r")
accesses = []
while True:
	inputLine = file.readline()
	if inputLine == "":
		break
	inputLine = inputLine.rstrip('\n')
	#print(inputLine)
	accesses.append(inputLine)
file.close()

#print(accesses)
for value in accesses:
	print(value)