def create_generator():
	my_values = range(3)
	print("myList is created")
	for i in my_values:
		print("pass here")
		yield i

for i in create_generator():
	print(i)