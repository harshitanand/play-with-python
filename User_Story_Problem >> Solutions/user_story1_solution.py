from collections import defaultdict

account_number = []

cell_values = {
	' _ | ||_|': '0',
	'     |  |': '1',
	' _  _||_ ': '2',
	' _  _| _|': '3',
	'   |_|  |': '4',
	' _ |_  _|': '5',
	' _ |_ |_|': '6',
	' _   |  |': '7',
	' _ |_||_|': '8',
	' _ |_| _|': '9',
}
def parse(image):
	structures = defaultdict(str)
	for ln in image.split('\n'):
		i = 0
		for m, img in enumerate(ln):
			if m%3 == 0:
				i = i+1
			structures[i] += img

	for char in structures.values():
			account_number.append(cell_values.get(char, '?'))

	return ''.join(account_number) 
