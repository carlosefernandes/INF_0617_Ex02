import sys

large_diff = 0
result = ""
for line in sys.stdin:
	for line in sys.stdin:
		diff, info = line.split(':')
		diff = float(diff)
		if (diff > large_diff):
			info = info.replace("\n","")
			result = info+ ", " +str(diff)
print(result)
