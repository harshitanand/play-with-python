import sys

lines = sys.stdin.readlines()
line = []

def output():
	for i in range(len(lines)):
		if i==0:
			queries = int(lines[0].rstrip())
		if queries>100 & len(lines[i])>200:
			break
		if i>0:
			whole = str(len(lines[i].rstrip()))
			line = lines[i].rstrip().split('.')
			line[1] = line[1].translate(None, 'aeiou')     # use re.sub('[aeiou]', '', line[1])
			site = str(len(line[1])+4)
			print site + "/" + whole

output()
