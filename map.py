
import sys
import re
for line in sys.stdin:
	columns = line.split()
	if (re.match("-9+.0+", columns[10]) or re.match("-9+.0+", columns[11])): continue;
	result = columns[10] + ":" + columns[11] + ":" + columns[3]+ " " + columns[2] + ", (" + columns[6]+ ", " + columns[7] + ")"
	print(result)