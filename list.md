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
