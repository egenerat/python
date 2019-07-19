## Package
Upgrade a pip package
```pip install Django --upgrade```

## Recursivity
By default, the maximum recursion depth is 1000.
To prevent the error `RuntimeError: maximum recursion depth exceeded`

The limit can be increased via
```
sys.setrecursionlimit(3000)
```
