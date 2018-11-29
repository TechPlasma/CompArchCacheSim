

test = ["a","b","c"]
testQue = ["b","a","c"]
print(test)
print(testQue)
test.remove(testQue.pop())
test.append("d")
testQue.insert(0,"d")
print(len(test))
print(testQue)
