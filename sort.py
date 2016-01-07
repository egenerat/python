# simple list
simple_list = [0, 9, -1, 3]

sorted_list = sorted(simple_list)
print(sorted_list)
# [-1, 0, 3, 9]

# in decreasing/reverse order
sorted_list = sorted(simple_list, reverse = True)
print(sorted_list)
# [9, 3, 0, -1]

# list of dictionaries
list_of_dictionaries = [{
		'name': 'alice',
		'age': 30
	},
	{
		'name': 'bob',
		'age': 20
	}
]
sorted_list = sorted(list_of_dictionaries, key=lambda x: x['age'])
print(sorted_list)
# [{'name': 'bob', 'age': 20}, {'name': 'alice', 'age': 30}]

# sort elements in a dictionary
dictionary_to_sort = {
	'val1': 4,
	'val2': 6,
	'val3': 1
}

# It is not possible to order a dictionary. The dictionary is first transformed as a tuple
# order by key: x[0]
sorted_tuples = sorted(dictionary_to_sort.items(), key=lambda x:x[0])
print(sorted_tuples)
# [('val1', 4), ('val2', 6), ('val3', 1)]

# order by value x[1]
sorted_tuples = sorted(dictionary_to_sort.items(), key=lambda x:x[1])
print(sorted_tuples)
# [('val3', 1), ('val1', 4), ('val2', 6)]


# complex structure
complex_dictionary = {
	'catC': {
		'value': 4,
		'obj': []
	},
	'catB': {
		'value': 2,
		'obj': []
	},
	'catA': {
		'value': 3,
		'obj': []
	},
}
print(complex_dictionary.items())
sorted(complex_dictionary.items(), key=lambda x:x[1])
