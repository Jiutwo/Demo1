for i in range(1,101):
	if i % 7 == 0:
		continue
	elif str(i)[0] == '7':
		continue
	elif str(i)[-1] == '7':
		continue
	print(i)
