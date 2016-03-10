f = open("input.txt", 'r')
lines = f.read().splitlines()
# find a program that makes each line a variable

f.close()

print(lines)

f = open("output.txt", 'r+')

for line in lines:
	length = len(line)
	if length >	10:
		f.write(line[0:10])
		newLine = line[0:10]
		print(newLine)
	if length <=10:
		f.write(line)
		print(line)

f.close()


# open the input file & read
# read the lines of the file
# read the length of each individual line in the file
# close input file
# print the lines
# open the output text & read/write
# write the lines of the input into the output
# if the length of a line is less then 10, print line
# run this for every line
# if the length is greater then 10, delete letters until length == 10
# f.close()