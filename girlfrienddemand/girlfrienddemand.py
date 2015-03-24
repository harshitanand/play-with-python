s = raw_input()
ln = len(s)
t = int(raw_input())

while t>0:
	t -= 1
	a, b = map(int, raw_input().split())
	a -= 1
	b -= 1
	a %= ln
	b %= ln
	if s[a] == s[b]:
		print "Yes"
	else:
		print "No"
