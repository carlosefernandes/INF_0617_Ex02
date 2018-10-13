import sys

large_diff = 0
result = ""
for line in sys.stdin:
	diff, info = line.split(':')
	diff = float(diff)
	# limit the large difference to 15oC
	if (diff > large_diff and diff < 15):
		large_diff = diff
		info = info.replace("\n","")
		result = info+ ", " +str(diff)
print(result)
