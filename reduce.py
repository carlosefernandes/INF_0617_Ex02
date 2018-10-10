import sys

large_diff = 0
result = ""
for line in sys.stdin:
	x1, x2, info = line.split(':')
	diff = float(x1) - float(x2)
	if (diff > large_diff):
		info = info.replace("\n","")
		result = info+ ", " +str(diff)
print(result)
