

test = ["a","b","c"]
testQue = ["b","a","c"]
print(test)
print(testQue)
test.remove(testQue.pop())
test.append("d")
testQue.insert(0,"d")
print(len(test))
print(testQue)

hexdata = "4b"

scale = 16 ## equals to hexadecimal

num_of_bits = 48

print(bin(int(hexdata, scale))[2:].zfill(num_of_bits))