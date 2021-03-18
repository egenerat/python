Find position of character
```
>>> "abc".find('c')
2
```

Left align
```
>>> "abc".ljust(5, '-')
'abc--'
```
Same with `rjust`

Specific case fill with zeros
```
>>> "1".zfill(3)
'001'
```

```
>>> "ABC".title()
'Abc'
```

```
>>> "1".isnumeric()
True
```

Also works with `isalnum`, `isalpha` and `isspace`
Format: `islower`, `isupper`

To change one character in a string (immutable), convert to list first
```
>>> list("abcd")
['a', 'b', 'c', 'd']
```


Strip functions
```
>>> "  abc  ".strip()
'abc'
```

Which is equivalent to strip(" ")

Strip only on the left with `lstrip`, only on the right with `rstrip`


Apply a function to all the characters in a string
```
>>> sum(map(int, list("123")))
6
```

Replace all
```
>>> "aaa _ bbb _ ccc".replace("_", "+")
'aaa + bbb + ccc'
```

Replace one
```
>>> "aaa _ bbb _ ccc".replace("_", "+", 1)
'aaa + bbb _ ccc'
```

Format amount
```
>>> "{:,}".format(1234567)
1,234,567
```
