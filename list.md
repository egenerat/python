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
