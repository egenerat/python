import re

string = 'a<tr>bcd</tr>ef\nab<tr>cdefabcd</tr>ef'
p1 = re.compile('<tr>([.\n\r\s\S+]*)</tr>')
p2 = re.compile('<tr>([.\n\r\s\S+]*?)</tr>')
result = re.findall(p1, string)
print(result)
result = re.findall(p2, string)
print(result)