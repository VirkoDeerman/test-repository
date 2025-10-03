def is_palindrome() -> bool:
	if usput := ''.join(char for char in input('\nEnter something:\n> ').lower() if char.isalpha()):
		return usput == usput[::-1]
	else:
		raise SystemExit('No imput provided, ending the program.')
while True:
	print('Yep, it\'s a palindrome, the thing you wrote.' if is_palindrome() else 'Nah, that wasn\'t a palindrome, nuh huh.'):
	pass
