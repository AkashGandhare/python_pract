my_list = [1,2,3]

for item in my_list:
	print("item = {}".format(item))

##tupel unpacking

my_list = [(1,2), (3,4), (5,6)]

for (a,b) in my_list:
	print(f"{a}")
	print(f"{b}")
	print(f"{a},{b}")

#for loop in dictinary

my_dict = {'key1':8, 'key2': 9, 'key3': 10}

for key,value in my_dict.items():
	print(key)
	print(value)