f = open("input.txt", 'r')
lines = f.read()
length = f.tell()

f.close()

print(lines)

# f = open("output.txt", 'r+')
# if length <10
	