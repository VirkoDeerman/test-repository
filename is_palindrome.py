def is_palindrome() -> bool | None:
	if usput := ''.join(char for char in input('\nEnter literally anything:\n> ').lower() if char.isalpha()):
		return usput == usput[::-1]
	else:
		raise ValueError

while True:
	try:
		print('\nYep, it\'s a palindrome, the thing you wrote.' if is_palindrome() else '\nNah, that wasn\'t a palindrome, nuh huh.')
	except ValueError:
		usput: str = input('\nConfirm exit\n> ').strip().lower()
		if not usput if not usput else usput[0] in 'ye':
			break