f = open("input.txt", 'r')
lines = f.read()
length = f.tell()

f.close()

print(lines)

f = open("output.txt", 'r+')
f.write(lines)

f.close()

print(lines)


# if length <10
	