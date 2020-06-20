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
