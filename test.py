'''
# Read input from stdin and provide input before running code

name = raw_input('What is your name?\n')
print 'Hi, %s.' % name
'''
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







		1.
Skipping Sum
Max. Marks 100

You are given an array of N integers A[1] , A[2] , ... , A[N] . You have to answer Q queries. Each query consists of 3 integers L, R and K. For each query, you have to find the value of the Skipping Sum in the following manner :

       def skipping_sum(L,R,K) :
              sum = 0
              while L <= R :
                    sum = sum + A[L]
                    L = L + K
              return sum

Input
The first line consists of 2 space separated integers N and Q. The next line consists of N space separated integers, the ith integer being A[i]. Then, Q lines follow, each line consisting of 3 space separated integers L, R and K.

Output
Print the answer to each query on a new line.

Constraints
1 ≤ N ≤ 105
1 ≤ Q ≤ 105
0 ≤ A[i] ≤ 105
1 ≤ L ≤ R ≤ N
1 ≤ K ≤ 10

NOTE:
We are using 1-based indexing for array A.
Sample Input (Plaintext Link)

8 6
5 4 2 1 7 9 10 9
1 8 1
1 8 2
4 8 9
3 7 2
3 7 3
3 7 4

Sample Output (Plaintext Link)

47
24
1
19
11
12
