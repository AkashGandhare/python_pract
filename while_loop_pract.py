num = 0

while num <= 5:
	print(f'number is {num}')
	num += 1
else:
	print('\n')
	print(f'number is greater than 5')


##continue, pass and break 
print('continue test')

x = 0;
while x < 5:
	pass
	x += 1

# x = 0;
# while x < 5:	
# 	if x == 2:
# 		x += 1
# 		continue

# x = 0;
# while x < 5:	
# 	if x == 2:
# 		x += 1
# 		continue
	
# 	print(f'number = {x}')
# 	x += 1

x = 0;
while x < 5:
	if x == 2:
		break;

	print(f'number = {x}')
	x += 1

		
