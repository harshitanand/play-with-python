from user_story1_solution import parse
from user_story2_solution import verify_account_no

final = {None: 'ILL',
		True: '',
		False: 'ERR'
}

def print_report(acc_no):
	result = []
	for i in acc_no:
		account_number = parse(i)
		valid = "ILL"
		if "?" not in account_number:
			valid = verify_account_no(account_number)
		result.append((final[valid], account_number))

	return result
