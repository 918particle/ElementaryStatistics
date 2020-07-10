import sys
import numpy as np

data_file = open(sys.argv[1])
stems = np.arange(0,10,1)
leaves = []
[leaves.append([]) for k in range(0,10)]
for i in data_file:
	firstDigit = int(i[0])
	for j in stems:
		if(int(firstDigit) == j):
			leaves[j].append(float(i[1:]))
			break
data_file.close()

print("\\begin{table}")
print("\\begin{tabular}{| c | c |}")
print("\\hline")
print("\\hline")
print("Stem & Leaves \\\\ \\hline")
for i in range(0,10):
	if(leaves[i]):
		result = str(stems[i])+" & "+str(leaves[i])+" \\\\ \\hline"
		print(result)
	else:
		result = str(stems[i])+" & "+" "+" \\\\ \\hline"
		print(result)
print("\\hline")
print("\\end{tabular}")
print("\\caption{}")
print("\\end{table}")