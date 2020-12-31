# List

## Instantiation
### One-dimensional list
```
>>> [None]*3
[None, None, None]
```


### Two-dimensional list
```
>>> [[None for x in range(3)] for y in range(2)]
[[None, None, None], [None, None, None]]
```

Be very careful
```
>>> ll = [[None]*3]*2
>>> ll
[[None, None, None], [None, None, None]]
```
But
```
>>> ll[0][2] = "Hello"
>>> ll
[[None, None, 'Hello'], [None, None, 'Hello']]
```
All the lines are referring to the same list


## Operations
remove()
```
list.remove('value')
```
returns the first matching

Iterate over indexes and values
```
for idx, val in enumerate(lst):
    print(f"{idx} {val}")
```

Count the number of occurrences in a list
Instead of checking if the key is in the dictionary, then increment
```
occ = {}
    for i in lst:
        if i not in occ:
            occ[i] = 0
        occ[i] += 1
```

We can use setdefault method
```
available.setdefault(key, value)
```

Sort on a function
```
sorted(lst, key=abs)
```

Sort tuples by second field
```
d.sort(key=lambda x: x[1])
```

Sort list on different fields
```
s = sorted(l, key=lambda x: (x[1], x[3], x[2]))
```

Reverse sort: `reverse=True` (available on `sorted()` and `.sort()`)


## Copy
```
>>> a = [[0]*3 for i in range(2)]
>>> a
[[0, 0, 0], [0, 0, 0]]
>>> b = a.copy()
>>> a[1][1] = 1
>>> b
[[0, 0, 0], [0, 1, 0]]
```
copy() is a shallow copy

To have a deep copy
```
>>> import copy
>>> a = [[0]*3 for i in range(2)]
>>> b = copy.deepcopy(a)
>>> a[1][1] = 1
>>> a
[[0, 0, 0], [0, 1, 0]]
>>> b
[[0, 0, 0], [0, 0, 0]]
```
