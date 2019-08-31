country = input('Your country is: ')
age = input ('Your age is: ')
age = int(age)
if country == 'Taiwan':
	if age >= 18:
		print('legal age for driving')
	else:
		print('You are not allowed to drive')
elif country == 'USA':
	if age >= 16:
		print('legal age for driving')
	else:
		print('You are not allowed to drive')
else:
	print('Sorry we have no legal information about your country')