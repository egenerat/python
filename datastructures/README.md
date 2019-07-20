### Documentation
https://docs.python.org/3/tutorial/datastructures.html

### Array

- Initialize an array of 3 elements (None)
```
>>> [None] * 3
[None, None, None]
```

- Expand array (spread, splat operator)
```
>>> [*[1, 2], *[3, 4]]
[1, 2, 3, 4]
```

Equivalent to
```
[1, 2] + [3, 4]
```
and
```
[1, 2].extend([3, 4])
```
