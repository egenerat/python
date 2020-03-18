# Random notes

## Virtual environnments
```
python3 -m venv venv
source venv/bin/activate
```

## Shebang
```
#!/usr/bin/env python3
```
To be replaced with python2 if needed

## Run a simple web server
```
python3 -m http.server
```

## Jupyter

[Documentation on jupyter.org](https://jupyter.org/index.html)
```
pip install jupyterlab
jupyter notebook
```

`Shift + Enter` to run a command

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

## Print without carriage return
```
print("message", end=" ")
```
Will use a space instead of a carriage return at the end of the message


# Code linting

## Pyflakes
https://pypi.org/project/pyflakes/
```
pip install pyflakes
pyflakes file.py
```

Unused imports
```
pyflakes app/**/*.py | grep "imported but unused"
```

## 2to3: Automated Python 2 to 3 code translation 
https://docs.python.org/2/library/2to3.html
```
2to3 -w file.py
```
