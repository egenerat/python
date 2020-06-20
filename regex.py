import re

pattern = 'hello'
string1 = 'hello world'
string2 = 'Hello world'

# Compile a regular expression pattern into a regular expression object
p = re.compile(pattern)
print(p.match(string1))
#

print(p.match(string2))
# None

# Compile the same pattern with IGNORECASE flag
p_ignore_case = re.compile(pattern, re.IGNORECASE)
print(p_ignore_case.match(string2))
# match!

# Determine if the RE matches at the beginning of the string.
print(p_ignore_case.match(' Hello'))
# None
print(p_ignore_case.search(' Hello'))
# match!

# find a pattern without compilation
string1 = 'to Alice and Bob from'
print(re.search('to .* from', string1))
# match


```
>>> re.findall("(\d+)", "07 23 32 32")
['07', '23', '32', '32']
```
