def is_palindrome() -> bool:
	usput: str = input('Enter a single word:\n> ').split()[0].lower()
	return usput[::len(usput)] == usput