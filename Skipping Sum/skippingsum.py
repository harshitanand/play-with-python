import sys

arr = []
queries = []
result = []
lines = sys.stdin.readlines()

def skipping_sum(L,R,K):
	sum = 0
	L = L-1
	while L < R:
		sum = sum + arr[L]
		L = L + K
	print sum

for i in range(len(lines)):
	if i==0:
		(arr_len, query) = lines[i].rstrip().split(' ')
	if i==1:
		arr = lines[i].rstrip().split(' ')
		arr = map(int, arr)
	if i>1:
		(L, R, K) = lines[i].rstrip().split(' ')
		L = int(L)
		R = int(R)
		K = int(K)
		skipping_sum(L,R,K)
