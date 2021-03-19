password = 'a123456'
i = 3
while i > 0:
	i -=1
	pd = input('Enter the password: ')
	if pd == password:
		print('Password currect! Success! ')
		break
	else:
		if i == 0:
			break
		else:
			print(i, 'chance left')
# test upload new version
	