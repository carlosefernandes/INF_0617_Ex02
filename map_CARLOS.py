import sys
import re

for line in sys.stdin:
	columns = line.split()
	if (not re.match("-9+.0+", columns[10]) and not re.match("-9+.0+", columns[11])):
		temp_diff = float(columns[10]) - float(columns[11])
		result = str(temp_diff) + ":" + columns[3]+ " " + columns[2] + ", (" + columns[6]+ ", " + columns[7] + ")"
		print(result)
