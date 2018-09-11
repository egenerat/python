elements = (i for i in [1, 2, 3])

for i in elements:
	print("Generator (first): {}".format(i))
for i in elements:
	print("Generator (second): {}".format(i))

elements = [i for i in [1, 2, 3]]

for i in elements:
	print("Array (first): {}".format(i))
for i in elements:
	print("Array (second): {}".format(i))
