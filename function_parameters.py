def arg_default_value(retries=None):
	if retries is None:
		retries = 4
	return retries

print(arg_default_value()) // 4
print(arg_default_value(1)) // 1

def f(L=None):
    if L is None:
        L = []
    L.append(2)
    return L

print(f(['1']))
print(f())

http://stackoverflow.com/questions/13087344/python-function-default-parameter-is-evaluated-only-once
https://docs.python.org/2/tutorial/controlflow.html#unpacking-argument-lists