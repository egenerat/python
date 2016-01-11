walk_dir = "/home/user/"

import os
result = [os.path.join(root, f) for root, subdirs, files in os.walk(walk_dir) for f in files if os.path.splitext(f)[1] == '.csv']
print(result)