import time

l = []
s = set()
NB_ELEMENTS = 20000000

print("- Create structure and insert {:,} elements".format(NB_ELEMENTS))

# Insertion in a list
start = time.time()
for i in range(NB_ELEMENTS):
    l.append(i)
end = time.time()
print("In a list: {}s".format(end - start))

# Insertion in a set
start = time.time()
for i in range(NB_ELEMENTS):
    s.add(i)
end = time.time()
print("In a set: {}s".format(end - start))

# Search for one element
print("\n- Search for one element")
ELT = 1234567

start = time.time()
ELT in l
end = time.time()
print("In a list: {}s".format(end - start))

start = time.time()
ELT in s
end = time.time()
print("In a set: {}s".format(end - start))